<template>
  <div class="bg-zinc-800 w-full rounded-xl p-4">
    <h3 class="text-xl font-extralight mb-2">Views by {{ viewType }}</h3>
    <p class="italic text-zinc-300 text-sm" v-if="!views.length">
      No data available
    </p>
    <ul class="rounded-lg">
      <li
        v-for="(view, index) in views"
        :key="index"
        class="flex justify-between border-t-2 border-zinc-700 py-2"
      >
        <span class="text-zinc-200 break-all w-2/3">{{ view.key }}</span>
        <span class="text-right text-zinc-400 font-extralight w-1/3">
          {{ view.count }} Views
        </span>
      </li>
    </ul>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
export default Vue.extend({
  name: 'WidgetViews',
  props: {
    views: {
      type: Array,
      required: true,
    },
    viewType: {
      type: String,
      required: true,
    },
  },
});
</script>
