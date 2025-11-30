module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  darkMode: 'class', 
  theme: {
    extend: {
      colors: {
        'surface': 'var(--surface)',
        primary: {
          50: '#f8f7ff',
          100: '#efeefe',
          200: '#d9d3fb',
          300: '#c2b7f7',
          400: '#9f86f1',
          500: '#7b56ea', 
          600: '#6a3fd1',
          700: '#562fa9',
          800: '#3f1f78',
          900: '#2a0f46'
        },
        accent: {
          500: '#2aa7f7'
        }
      },
      boxShadow: {
        'card': '0 6px 18px rgba(11,7,28,0.45)',
      }
    },
  },
  plugins: [],
}
