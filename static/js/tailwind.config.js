module.exports = {
  content: ["./templates/**/*.html"],
  theme: {
    extend: {
      colors: {
        background: {
          DEFAULT: '#FFFFFF',
          warm: '#FAFAF9',
          soft: '#F6F7F9',
        },
        surface: {
          DEFAULT: '#FFFFFF',
          border: '#E7E9EE',
        },
        text: {
          primary: '#172033',
          secondary: '#4B5565',
          muted: '#7B8494',
        },
        navy: {
          DEFAULT: '#172A46',
          light: '#223B5D',
        },
        brand: {
          purple: '#74358F',
          violet: '#8D4BA6',
          magenta: '#C45A91',
          rose: '#D979A0',
        }
      },
      fontFamily: {
        sans: ['Inter', 'Noto Sans Arabic', 'sans-serif'],
      },
      boxShadow: {
        subtle: '0 8px 30px rgba(20, 30, 50, 0.04)',
      }
    },
  },
  plugins: [],
}