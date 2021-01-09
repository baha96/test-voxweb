module.exports = {
  theme: {
    screens: {
      sm: '640px',
      md: '767px',
      lg: '992px',
      xl: '1200px',
      xxl: '1440px',
    },
    colors: {
      blue: '#545DA7',
      white: '#fff'
    },
    backgroundColor: theme => theme('colors'),
    spacing: {
      px: '1px',
      '0': '0',
      '0.5': '0.5rem',
      '0.7': '0.7rem',
      '0.8': '0.8rem',
      '1': '1rem',
      '1.2': '1.2rem',
      '1.5': '1.5rem',
      '1.8': '1.8rem',
      '2': '2rem',
      '2.2': '2.2rem',
      '2.5': '2.5rem',
      '2.8': '2.8rem',
      '3': '3rem',
      '3.2': '3.2rem',
      '3.5': '3.5rem',
      '3.8': '3.8rem',
      '4': '4rem',
      '4.2': '4.2rem',
      '4.5': '4.5rem',
      '4.8': '4.8rem',
      '5': '5rem',
      '5.2': '5.2rem',
      '5.5': '5.5rem',
      '5.8': '5.8rem',
      '6': '6rem',
      '6.2': '6.2rem',
      '6.5': '6.5rem',
      '6.8': '6.8rem',
    },
    margin: (theme, {negative}) => ({
      auto: 'auto',
      ...theme('spacing'),
      ...negative(theme('spacing')),
    }),
    borderRadius: {
      default: '4px',
      '50': '50px'
    },
    boxShadow: {
      default: '0px 2px 8px rgba(0, 0, 0, 0.135216)',
      '1': '3px 2px 20px rgba(84, 93, 167, 0.5)',
    },
    extend: {
      width: {
        '1.5/2': '49%',
      }
    }
  },
  corePlugins: {
    fontFamily: false,
  },
  variants: {},
  plugins: [],  
  purge: {
    enabled: process.env.NODE_ENV === 'production',
    content: [
      'components/**/*.vue',
      'layouts/**/*.vue',
      'pages/**/*.vue',
      'plugins/**/*.js',
      'nuxt.config.js',
      // TypeScript
      'plugins/**/*.ts',
      'nuxt.config.ts'
    ]
  }
}
}
