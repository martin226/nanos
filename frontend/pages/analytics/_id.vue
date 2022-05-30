<template>
  <div class="space-y-6">
    <div class="bg-zinc-800 w-full rounded-xl space-y-2 p-4">
      <h3 class="text-xl font-extralight">
        Analytics for
        <a
          :href="'/' + data.short_url"
          target="_blank"
          class="underline underline-zinc-600"
          >{{ data.short_url }}</a
        >
      </h3>
      <p class="text-zinc-200">
        Original URL:
        <span class="text-zinc-400 font-extralight">{{ data.url }}</span>
      </p>
      <p class="text-zinc-200">
        Total Views:
        <span class="text-zinc-400 font-extralight">{{ data.views }}</span>
      </p>
      <p class="text-zinc-200">
        Unique Views:
        <span class="text-zinc-400 font-extralight">{{
          data.unique_views
        }}</span>
      </p>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
      <WidgetViews :views="data.country_views" view-type="Country" />
      <WidgetViews :views="data.referrer_views" view-type="Referrer" />
      <WidgetViews :views="data.device_views" view-type="Device" />
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
export default Vue.extend({
  name: 'AnalyticsPage',
  async asyncData({ params, store }) {
    const { id } = params;
    const data = await store.dispatch('getAnalytics', id);
    return { data };
  },
});
</script>
