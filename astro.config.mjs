import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://chumbo.io',
  integrations: [sitemap({
    filter: (page) => !page.includes('/admin'),
  })],
  output: 'static',
});

