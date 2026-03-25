import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

import cloudflare from '@astrojs/cloudflare';

export default defineConfig({
  site: 'https://chumbo.io',
  integrations: [sitemap()],
  output: 'static',
  adapter: cloudflare(),
});