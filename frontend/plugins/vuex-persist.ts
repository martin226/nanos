import { VuexPersistence } from 'vuex-persist';
import { Plugin } from '@nuxt/types';

const vuexPersist: Plugin = ({ store }) => {
  new VuexPersistence().plugin(store);
};

export default vuexPersist;
