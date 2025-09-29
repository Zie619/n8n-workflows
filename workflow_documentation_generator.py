#!/usr/bin/env python3
"""
n8n Workflow Documentation Generator
Generates comprehensive documentation for workflows including API docs, usage guides, and deployment instructions
"""

import json
import os
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any
import re

class WorkflowDocumentationGenerator:
    def __init__(self, workflows_dir="workflows"):
        self.workflows_dir = Path(workflows_dir)
        self.documentation_templates = {
            'api_docs': self.generate_api_documentation,
            'usage_guide': self.generate_usage_guide,
            'deployment_guide': self.generate_deployment_guide,
            'troubleshooting': self.generate_troubleshooting_guide
        }
        
    def extract_workflow_metadata(self, workflow_data: Dict) -> Dict[str, Any]:
        """Extract comprehensive metadata from workflow"""
        nodes = workflow_data.get('nodes', [])
        connections = workflow_data.get('connections', {})
        
        metadata = {
            'name': workflow_data.get('name', 'Unnamed Workflow'),
            'description': workflow_data.get('description', ''),
            'total_nodes': len(nodes),
            'node_types': list(set(node.get('type', '') for node in nodes)),
            'trigger_types': [],
            'integrations': [],
            'credentials_needed': set(),
            'environment_variables': set(),
            'webhook_endpoints': [],
            'api_endpoints': [],
            'error_handling': False,
            'complexity_level': 'simple',
            'execution_time_estimate': 'unknown'
        }
        
        # Analyze nodes for metadata
        for node in nodes:
            node_type = node.get('type', '')
            
            # Check for triggers
            if any(trigger in node_type.lower() for trigger in ['trigger', 'webhook', 'schedule', 'cron']):
                metadata['trigger_types'].append(node_type)
                
                # Extract webhook info
                if 'webhook' in node_type.lower():
                    webhook_id = node.get('webhookId', '')
                    path = node.get('parameters', {}).get('path', '')
                    if webhook_id or path:
                        metadata['webhook_endpoints'].append({
                            'id': webhook_id,
                            'path': path,
                            'method': node.get('parameters', {}).get('httpMethod', 'POST')
                        })
            
            # Check for integrations
            integration_types = ['slack', 'github', 'google', 'microsoft', 'salesforce', 'hubspot', 'stripe', 'zendesk']
            for integration in integration_types:
                if integration in node_type.lower():
                    metadata['integrations'].append(integration.title())
            
            # Extract credentials
            credentials = node.get('credentials', {})
            for cred_type in credentials.keys():
                metadata['credentials_needed'].add(cred_type)
            
            # Extract environment variables
            parameters = node.get('parameters', {})
            self.extract_env_variables(parameters, metadata['environment_variables'])
            
            # Check for error handling
            if 'error' in node_type.lower() or 'stop' in node_type.lower():
                metadata['error_handling'] = True
        
        # Determine complexity level
        if metadata['total_nodes'] <= 5:
            metadata['complexity_level'] = 'simple'
        elif metadata['total_nodes'] <= 15:
            metadata['complexity_level'] = 'moderate'
        else:
            metadata['complexity_level'] = 'complex'
        
        # Estimate execution time
        if metadata['total_nodes'] <= 5:
            metadata['execution_time_estimate'] = '1-5 seconds'
        elif metadata['total_nodes'] <= 15:
            metadata['execution_time_estimate'] = '5-30 seconds'
        else:
            metadata['execution_time_estimate'] = '30+ seconds'
        
        return metadata
    
    def extract_env_variables(self, obj, env_vars: set, path=""):
        """Recursively extract environment variables from workflow parameters"""
        if isinstance(obj, str) and obj.startswith('{{ $env.'):
            # Extract environment variable name
            match = re.search(r'\{\{\s*\$env\.(\w+)\s*\}\}', obj)
            if match:
                env_vars.add(match.group(1))
        elif isinstance(obj, dict):
            for key, value in obj.items():
                self.extract_env_variables(value, env_vars, f"{path}.{key}")
        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                self.extract_env_variables(item, env_vars, f"{path}[{i}]")
    
    def generate_api_documentation(self, workflow_data: Dict, metadata: Dict[str, Any]) -> str:
        """Generate API documentation for workflow"""
        docs = f"""# API Documentation: {metadata['name']}

## Overview
{metadata['description'] or 'Automated workflow for data processing and integration.'}

## Workflow Metadata
- **Total Nodes**: {metadata['total_nodes']}
- **Complexity Level**: {metadata['complexity_level'].title()}
- **Estimated Execution Time**: {metadata['execution_time_estimate']}
- **Error Handling**: {'✅ Implemented' if metadata['error_handling'] else '❌ Not implemented'}

## Trigger Information
"""
        
        if metadata['trigger_types']:
            docs += f"### Trigger Types\n"
            for trigger in metadata['trigger_types']:
                docs += f"- `{trigger}`\n"
        else:
            docs += "### Trigger Types\n- Manual trigger (no automatic triggers configured)\n"
        
        if metadata['webhook_endpoints']:
            docs += f"\n### Webhook Endpoints\n"
            for endpoint in metadata['webhook_endpoints']:
                docs += f"- **Path**: `{endpoint['path']}`\n"
                docs += f"- **Method**: `{endpoint['method']}`\n"
                docs += f"- **Webhook ID**: `{endpoint['id']}`\n\n"
        
        docs += f"""
## Node Types Used
"""
        for node_type in metadata['node_types']:
            docs += f"- `{node_type}`\n"
        
        docs += f"""
## Integrations
"""
        if metadata['integrations']:
            for integration in metadata['integrations']:
                docs += f"- {integration}\n"
        else:
            docs += "- No external integrations detected\n"
        
        docs += f"""
## Required Credentials
"""
        if metadata['credentials_needed']:
            for credential in metadata['credentials_needed']:
                docs += f"- `{credential}`\n"
        else:
            docs += "- No credentials required\n"
        
        docs += f"""
## Environment Variables
"""
        if metadata['environment_variables']:
            for env_var in metadata['environment_variables']:
                docs += f"- `{env_var}`\n"
        else:
            docs += "- No environment variables required\n"
        
        return docs
    
    def generate_usage_guide(self, workflow_data: Dict, metadata: Dict[str, Any]) -> str:
        """Generate usage guide for workflow"""
        guide = f"""# Usage Guide: {metadata['name']}

## Quick Start

### Prerequisites
"""
        
        if metadata['credentials_needed']:
            guide += f"1. **Configure Credentials**: Set up the following credentials in n8n:\n"
            for credential in metadata['credentials_needed']:
                guide += f"   - {credential}\n"
        
        if metadata['environment_variables']:
            guide += f"\n2. **Set Environment Variables**: Configure these environment variables:\n"
            for env_var in metadata['environment_variables']:
                guide += f"   - `{env_var}`\n"
        
        guide += f"""
### Deployment Steps

1. **Import Workflow**
   - Copy the workflow JSON into your n8n instance
   - Or import directly from the workflow file

2. **Configure Credentials**
   - Go to Settings > Credentials
   - Add all required credentials as identified above

3. **Set Environment Variables**
   - Configure in your n8n environment or `.env` file
   - Ensure all variables are properly set

4. **Test Workflow**
   - Run the workflow in test mode
   - Verify all nodes execute successfully
   - Check data flow and transformations

5. **Activate Workflow**
   - Enable the workflow for production use
   - Monitor execution logs for any issues

## Workflow Flow

This workflow consists of {metadata['total_nodes']} nodes with the following execution flow:

"""
        
        # Add basic flow description
        if metadata['trigger_types']:
            guide += f"1. **Trigger**: Workflow starts with {', '.join(metadata['trigger_types'])}\n"
        
        guide += f"2. **Processing**: Data flows through {metadata['total_nodes'] - len(metadata['trigger_types'])} processing nodes\n"
        
        if metadata['integrations']:
            guide += f"3. **Integration**: Connects with {', '.join(metadata['integrations'])}\n"
        
        guide += f"""
## Configuration Options

### Node Configuration
- Review each node's parameters
- Update any hardcoded values
- Configure retry and timeout settings

### Error Handling
{'✅ This workflow includes error handling nodes' if metadata['error_handling'] else '⚠️ Consider adding error handling nodes'}

### Performance Tuning
- Monitor execution time: {metadata['execution_time_estimate']}
- Optimize for your expected data volume
- Consider rate limiting for external APIs

## Troubleshooting

### Common Issues
1. **Credential Errors**: Verify all credentials are properly configured
2. **Environment Variable Issues**: Check that all required variables are set
3. **Node Execution Failures**: Review node logs for specific error messages
4. **Data Format Issues**: Ensure input data matches expected format

### Debug Mode
- Enable debug mode in n8n settings
- Check execution logs for detailed information
- Use test data to verify workflow behavior

## Best Practices
- Regularly monitor workflow execution
- Set up alerts for failures
- Keep credentials secure and rotate regularly
- Test changes in development environment first
"""
        
        return guide
    
    def generate_deployment_guide(self, workflow_data: Dict, metadata: Dict[str, Any]) -> str:
        """Generate deployment guide for workflow"""
        guide = f"""# Deployment Guide: {metadata['name']}

## Pre-Deployment Checklist

### ✅ Environment Setup
- [ ] n8n instance is running and accessible
- [ ] Required credentials are configured
- [ ] Environment variables are set
- [ ] Network connectivity to external services

### ✅ Workflow Validation
- [ ] Workflow JSON is valid
- [ ] All nodes are properly configured
- [ ] Connections are correctly established
- [ ] Error handling is implemented

### ✅ Security Review
- [ ] No sensitive data in workflow JSON
- [ ] Credentials use secure storage
- [ ] Webhook endpoints are secured
- [ ] Access controls are in place

## Deployment Methods

### Method 1: Direct Import
1. Copy the workflow JSON
2. In n8n, go to Workflows > Import
3. Paste the JSON content
4. Save and configure credentials

### Method 2: File Upload
1. Save workflow as `.json` file
2. Use n8n import functionality
3. Upload the file
4. Review and activate

### Method 3: API Deployment
```bash
# Example using n8n API
curl -X POST "http://your-n8n-instance/api/v1/workflows" \\
  -H "Content-Type: application/json" \\
  -H "Authorization: Bearer YOUR_API_KEY" \\
  -d @workflow.json
```

## Post-Deployment Configuration

### 1. Credential Setup
"""
        
        if metadata['credentials_needed']:
            guide += f"Configure these credentials in n8n:\n"
            for credential in metadata['credentials_needed']:
                guide += f"- **{credential}**: [Instructions for setting up {credential}]\n"
        else:
            guide += "No credentials required for this workflow.\n"
        
        guide += f"""
### 2. Environment Variables
"""
        
        if metadata['environment_variables']:
            guide += f"Set these environment variables:\n"
            for env_var in metadata['environment_variables']:
                guide += f"- `{env_var}`: [Description of what this variable should contain]\n"
        else:
            guide += "No environment variables required.\n"
        
        guide += f"""
### 3. Webhook Configuration
"""
        
        if metadata['webhook_endpoints']:
            guide += f"Configure webhook endpoints:\n"
            for endpoint in metadata['webhook_endpoints']:
                guide += f"- **Path**: `{endpoint['path']}`\n"
                guide += f"- **Method**: `{endpoint['method']}`\n"
                guide += f"- **URL**: `https://your-n8n-instance/webhook/{endpoint['path']}`\n\n"
        else:
            guide += "No webhook endpoints to configure.\n"
        
        guide += f"""
## Testing & Validation

### 1. Test Execution
- Run workflow in test mode
- Verify all nodes execute successfully
- Check data transformations
- Validate output format

### 2. Integration Testing
- Test with real data sources
- Verify external API connections
- Check error handling scenarios
- Monitor performance metrics

### 3. Load Testing
- Test with expected data volume
- Monitor execution time
- Check resource usage
- Verify scalability

## Monitoring & Maintenance

### Monitoring Setup
- Enable execution logging
- Set up performance monitoring
- Configure error alerts
- Monitor webhook usage

### Maintenance Tasks
- Regular credential rotation
- Update API endpoints if needed
- Monitor for deprecated nodes
- Review and optimize performance

### Backup & Recovery
- Export workflow regularly
- Backup credential configurations
- Document custom configurations
- Test recovery procedures

## Production Considerations

### Security
- Use HTTPS for webhook endpoints
- Implement proper authentication
- Regular security audits
- Monitor access logs

### Performance
- Expected execution time: {metadata['execution_time_estimate']}
- Monitor resource usage
- Optimize for your data volume
- Consider rate limiting

### Reliability
- Implement retry logic
- Set up monitoring alerts
- Plan for disaster recovery
- Regular health checks
"""
        
        return guide
    
    def generate_troubleshooting_guide(self, workflow_data: Dict, metadata: Dict[str, Any]) -> str:
        """Generate troubleshooting guide for workflow"""
        guide = f"""# Troubleshooting Guide: {metadata['name']}

## Common Issues & Solutions

### 1. Workflow Won't Start

#### Issue: No trigger activation
**Symptoms**: Workflow doesn't execute automatically
**Solutions**:
- Check if workflow is active
- Verify trigger configuration
- Test trigger manually
- Check webhook URL accessibility

#### Issue: Credential errors
**Symptoms**: Nodes fail with authentication errors
**Solutions**:
- Verify credentials are properly configured
- Check credential expiration
- Test credentials independently
- Update credential values if needed

### 2. Node Execution Failures

#### Issue: HTTP Request failures
**Symptoms**: HTTP nodes return error codes
**Solutions**:
- Check URL accessibility
- Verify request format
- Check authentication headers
- Review rate limiting

#### Issue: Data format errors
**Symptoms**: Nodes fail with parsing errors
**Solutions**:
- Verify input data format
- Check data transformations
- Validate JSON structure
- Use data validation nodes

#### Issue: API rate limiting
**Symptoms**: External API calls fail with rate limit errors
**Solutions**:
- Implement delay nodes
- Use batch processing
- Check API quotas
- Optimize request frequency

### 3. Performance Issues

#### Issue: Slow execution
**Symptoms**: Workflow takes longer than expected
**Solutions**:
- Monitor node execution times
- Optimize data transformations
- Use parallel processing where possible
- Check external service performance

#### Issue: Memory issues
**Symptoms**: Workflow fails with memory errors
**Solutions**:
- Reduce data volume per execution
- Use pagination for large datasets
- Optimize data structures
- Consider workflow splitting

### 4. Data Flow Issues

#### Issue: Missing data
**Symptoms**: Expected data not available in nodes
**Solutions**:
- Check data source connectivity
- Verify data filtering logic
- Review conditional nodes
- Check data mapping

#### Issue: Incorrect data format
**Symptoms**: Data doesn't match expected format
**Solutions**:
- Add data validation nodes
- Check data transformations
- Verify API response format
- Use data type conversion

## Debugging Techniques

### 1. Enable Debug Mode
- Go to n8n Settings > Logging
- Enable debug mode
- Review detailed execution logs
- Check node-specific error messages

### 2. Test Individual Nodes
- Run nodes in isolation
- Use sample data for testing
- Verify node configurations
- Check input/output formats

### 3. Use Execution History
- Review past executions
- Compare successful vs failed runs
- Check execution data
- Identify patterns in failures

### 4. Monitor External Services
- Check API status pages
- Verify service availability
- Monitor response times
- Check error rates

## Error Codes Reference

### HTTP Status Codes
- **400**: Bad Request - Check request format
- **401**: Unauthorized - Verify credentials
- **403**: Forbidden - Check permissions
- **404**: Not Found - Verify URL/endpoint
- **429**: Too Many Requests - Implement rate limiting
- **500**: Internal Server Error - Check external service

### n8n Specific Errors
- **Credential Error**: Authentication issue
- **Data Error**: Format or validation issue
- **Connection Error**: Network or service unavailable
- **Execution Error**: Node configuration issue

## Prevention Strategies

### 1. Proactive Monitoring
- Set up execution monitoring
- Configure error alerts
- Monitor performance metrics
- Track usage patterns

### 2. Regular Maintenance
- Update credentials regularly
- Review and test workflows
- Monitor for deprecated features
- Keep documentation current

### 3. Testing Procedures
- Test with various data scenarios
- Verify error handling
- Check edge cases
- Validate recovery procedures

### 4. Documentation
- Keep troubleshooting guides updated
- Document known issues
- Record solutions for common problems
- Maintain change logs

## Getting Help

### Self-Help Resources
- n8n Documentation: https://docs.n8n.io
- Community Forum: https://community.n8n.io
- GitHub Issues: https://github.com/n8n-io/n8n/issues

### Support Contacts
- Check your n8n support plan
- Contact system administrator
- Escalate to technical team
- Use vendor support channels

## Emergency Procedures

### Workflow Recovery
1. Disable workflow immediately
2. Check system resources
3. Review error logs
4. Restore from backup if needed
5. Test in isolated environment
6. Re-enable with monitoring

### Data Recovery
1. Check execution history
2. Identify failed executions
3. Re-run with corrected data
4. Verify data integrity
5. Update downstream systems
"""
        
        return guide
    
    def generate_complete_documentation(self, workflow_path: Path) -> Dict[str, str]:
        """Generate complete documentation package for a workflow"""
        try:
            with open(workflow_path, 'r', encoding='utf-8') as f:
                workflow_data = json.load(f)
            
            metadata = self.extract_workflow_metadata(workflow_data)
            
            documentation = {
                'api_docs': self.generate_api_documentation(workflow_data, metadata),
                'usage_guide': self.generate_usage_guide(workflow_data, metadata),
                'deployment_guide': self.generate_deployment_guide(workflow_data, metadata),
                'troubleshooting_guide': self.generate_troubleshooting_guide(workflow_data, metadata)
            }
            
            return documentation
            
        except Exception as e:
            return {
                'error': f"Failed to generate documentation: {str(e)}"
            }
    
    def generate_documentation_for_all_workflows(self) -> Dict[str, Any]:
        """Generate documentation for all workflows"""
        print("📚 Generating documentation for all workflows...")
        
        documentation_results = {
            'timestamp': datetime.now().isoformat(),
            'total_workflows': 0,
            'documented_workflows': 0,
            'workflow_documentation': {},
            'summary': {}
        }
        
        for category_dir in self.workflows_dir.iterdir():
            if category_dir.is_dir():
                category_name = category_dir.name
                
                for workflow_file in category_dir.glob('*.json'):
                    documentation_results['total_workflows'] += 1
                    
                    workflow_name = workflow_file.stem
                    print(f"   📝 Documenting: {workflow_name}")
                    
                    documentation = self.generate_complete_documentation(workflow_file)
                    
                    if 'error' not in documentation:
                        documentation_results['documented_workflows'] += 1
                        documentation_results['workflow_documentation'][workflow_name] = {
                            'category': category_name,
                            'documentation': documentation
                        }
                        
                        # Save individual documentation files
                        doc_dir = Path(f"documentation/{category_name}")
                        doc_dir.mkdir(parents=True, exist_ok=True)
                        
                        for doc_type, doc_content in documentation.items():
                            doc_file = doc_dir / f"{workflow_name}_{doc_type}.md"
                            with open(doc_file, 'w', encoding='utf-8') as f:
                                f.write(doc_content)
                    else:
                        print(f"   ❌ Error documenting {workflow_name}: {documentation['error']}")
        
        # Generate summary
        documentation_results['summary'] = {
            'success_rate': (documentation_results['documented_workflows'] / documentation_results['total_workflows'] * 100) if documentation_results['total_workflows'] > 0 else 0,
            'categories_covered': len(set(doc['category'] for doc in documentation_results['workflow_documentation'].values())),
            'documentation_types_generated': len(self.documentation_templates)
        }
        
        print(f"\n✅ Documentation generation complete!")
        print(f"   📊 Total workflows: {documentation_results['total_workflows']}")
        print(f"   📝 Documented workflows: {documentation_results['documented_workflows']}")
        print(f"   📁 Categories covered: {documentation_results['summary']['categories_covered']}")
        print(f"   📚 Documentation saved to: documentation/ directory")
        
        return documentation_results

def main():
    """Main documentation generation function"""
    generator = WorkflowDocumentationGenerator()
    results = generator.generate_documentation_for_all_workflows()
    
    # Save summary report
    with open("documentation_generation_report.json", "w") as f:
        json.dump(results, f, indent=2)
    
    print(f"\n📄 Documentation summary saved to: documentation_generation_report.json")
    print(f"\n🎉 Documentation generation complete!")

if __name__ == "__main__":
    main()
