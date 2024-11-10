/*
 * Copyright (c) 2024 ThrRip
 *
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at https://mozilla.org/MPL/2.0/.
 */

export default defineNuxtConfig({
  // Extensions
  modules: [
    '@nuxt/eslint'
  ],

  // Client
  app: {
    head: {
      htmlAttrs: { lang: 'en' },
      charset: 'utf-8',
      viewport: 'width=device-width, initial-scale=1',
      title: '"secret" decode'
    }
  },

  css: [
    '~/assets/css/main.css'
  ],

  // Development
  devServer: {
    host: '0.0.0.0'
  },

  // Feature flags
  future: {
    compatibilityVersion: 4
  },

  compatibilityDate: '2024-11-06',

  // Tooling
  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {}
    }
  },

  eslint: {
    config: {
      stylistic: true
    }
  }
})
