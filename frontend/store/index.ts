import { MutationTree, ActionTree } from 'vuex';

export const state = () => ({
  shortenHistory: [] as {
    short_url: string;
    analytics_id: string;
    url: string;
  }[],
});

export type RootState = ReturnType<typeof state>;

export const mutations: MutationTree<RootState> = {
  addShortenHistory(state, shortenData) {
    state.shortenHistory.push(shortenData);
  },
  clearShortenHistory(state) {
    state.shortenHistory = [];
  },
};

export const actions: ActionTree<RootState, RootState> = {
  async createLink({ commit }, url) {
    try {
      if (!url.startsWith('http')) url = `http://${url}`;
      const res = await this.$axios.$post('/api/create', { url });
      commit('addShortenHistory', { ...res, url });
      return res;
    } catch (e) {
      return null;
    }
  },
  async getAnalytics(_, id) {
    try {
      const res = await this.$axios.$get('/api/stats/' + id);
      return res;
    } catch (e) {
      return null;
    }
  },
};
