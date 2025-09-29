# Troubleshooting Guide: n8n Subworkflow Dependency Graph & Auto-Tagging

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
