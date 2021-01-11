const path = require("path");

export default {
  env: require("dotenv").config({path: process.env.NODE_ENV === 'development' ? '.env' : '.env.production'}),
  // Global page headers (https://go.nuxtjs.dev/config-head)
  head: {
    title: 'Test-voxweb',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },

  // Global CSS (https://go.nuxtjs.dev/config-css)
  css: [
    {src: '~assets/styles/main.scss', lang: 'scss'},
  ],

  server: {
    port: 7888,
  },

  // Plugins to run before rendering page (https://go.nuxtjs.dev/config-plugins)
  plugins: [
    'plugins/axios.js',
  ],

  // Auto import components (https://go.nuxtjs.dev/config-components)
  components: true,

  // Modules for dev and build (recommended) (https://go.nuxtjs.dev/config-modules)
  buildModules: [

  ],

  // Modules (https://go.nuxtjs.dev/config-modules)
  modules: [
    '@nuxtjs/axios',
    '@nuxtjs/style-resources',
  ],
  axios: {
    proxy: true,
    credentials: true,
  },
  proxy: {
    '/api' : process.env.NUXT_ENV_APP_PROXY
  },
  styleResources: {
    scss: [
      'assets/styles/modules/_variable.scss',
    ]
  },
  loading: {color: '#00B2A8'},
  // Build Configuration (https://go.nuxtjs.dev/config-build)
  build: {
    extend(config, {isDev, isClient}) {
      const alias = config.resolve.alias = config.resolve.alias || {};
      alias['@images'] = path.resolve(__dirname, "assets/images");
    }
  }
}
