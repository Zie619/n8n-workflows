import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  /* config options here */
  reactStrictMode: true,

  // Enable experimental features for better performance
  experimental: {
    // Optimize for serverless deployment
    serverActions: {
      bodySizeLimit: '2mb',
    },
  },

  // Image optimization
  images: {
    formats: ['image/avif', 'image/webp'],
    remotePatterns: [
      {
        protocol: 'https',
        hostname: '**.supabase.co',
        pathname: '/storage/v1/object/public/**',
      },
    ],
  },

  // TypeScript configuration
  typescript: {
    // Fail build on type errors in production
    ignoreBuildErrors: false,
  },

  // ESLint configuration
  eslint: {
    // Fail build on lint errors in production
    ignoreDuringBuilds: false,
  },
};

export default nextConfig;
