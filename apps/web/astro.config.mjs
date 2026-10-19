import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

export default defineConfig({
  site: 'https://example.invalid',
  base: '/',
  integrations: [starlight({
    title: 'AI Video Bible',
    defaultLocale: 'zh-tw',
    locales: { 'zh-tw': { label: '繁體中文', lang: 'zh-TW' }, en: { label: 'English', lang: 'en-US' } },
    // Use Starlight's locale-aware generated navigation instead of a stale
    // zh-TW-only CH01 link that pointed to a non-existent route.
    customCss: ['./src/styles/editorial.css'],
  })],
});
