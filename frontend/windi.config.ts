import { defineConfig } from '@windicss/plugin-utils';

export default defineConfig({
  /**
   * Write windi classes in html attributes.
   * @see https://windicss.org/features/attributify.html
   */
  plugins: [
    require('windicss/plugin/forms'),
    require('@windicss/plugin-scrollbar'),
  ],
});
