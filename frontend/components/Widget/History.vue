<template>
  <div v-if="shortenHistory.length" class="overflow-hidden space-y-4">
    <h3 class="text-xl font-extralight mt-4 ml-4">Nano History</h3>
    <div
      class="max-h-48 overflow-y-auto scrollbar-thin scrollbar-thumb-true-gray-600 scrollbar-track-zinc-700"
    >
      <ul class="rounded-lg">
        <li
          v-for="(shorten, index) in shortenHistory.slice().reverse()"
          :key="index"
          class="grid grid-cols-1 md:grid-cols-2 px-4 py-6 border-t-2 border-zinc-700 gap-4"
        >
          <div class="flex flex-col space-y-2">
            <a
              :href="shorten.short_url"
              target="_blank"
              class="text-lg font-extralight text-zinc-100"
              >{{ shorten.short_url }}</a
            >
            <span class="text-zinc-400">{{ shorten.url }}</span>
          </div>
          <div class="flex space-x-4 items-center justify-start md:justify-end">
            <a
              :href="shorten.short_url"
              target="_blank"
              class="bg-zinc-700 text-zinc-300 px-4 py-2 rounded-lg"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-5 xl:h-6 w-5 xl:w-6"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
                stroke-width="2"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M14 5l7 7m0 0l-7 7m7-7H3"
                />
              </svg>
            </a>
            <button
              class="bg-zinc-700 text-zinc-300 px-4 py-2 rounded-lg"
              @click="$copyText(shorten.short_url)"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-5 xl:h-6 w-5 xl:w-6"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
                stroke-width="2"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3"
                />
              </svg>
            </button>
            <NuxtLink
              :to="shorten.analytics_url"
              class="bg-zinc-700 text-zinc-300 px-4 py-2 rounded-lg"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-5 xl:h-6 w-5 xl:w-6"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
                stroke-width="2"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"
                />
              </svg>
            </NuxtLink>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import { mapState } from 'vuex';
import { RootState } from '@/store/index';

export default Vue.extend({
  name: 'WidgetHistory',
  computed: {
    ...mapState<RootState>({
      shortenHistory: (state: RootState) => {
        return state.shortenHistory.map((shorten) => {
          return {
            short_url: window.location.origin + '/' + shorten.short_url,
            analytics_url: '/analytics/' + shorten.analytics_id,
            url: shorten.url,
          };
        });
      },
    }),
  },
});
</script>
