<template>
  <form class="flex divide-x-2 divide-zinc-700" @submit.prevent="createLink">
    <input
      ref="url"
      v-model="url"
      type="text"
      placeholder="https://example.com"
      class="rounded-l-xl bg-zinc-800 text-zinc-300 focus:ring-gray-500 outline-none border-0 p-4 flex-grow"
    />
    <button class="rounded-r-xl px-8 py-4 bg-zinc-800 text-zinc-400">
      nano it!
    </button>
  </form>
</template>

<script lang="ts">
import Vue from 'vue';
export default Vue.extend({
  name: 'FormCreate',
  data() {
    return {
      url: '',
    };
  },
  methods: {
    async createLink() {
      const data = await this.$store.dispatch('createLink', this.url);
      if (!data) return;
      this.url = window.location.origin + '/' + data.short_url;
      this.$nextTick(() => {
        (this.$refs.url as HTMLInputElement).select();
      });
    },
  },
});
</script>
