<template>
  <div class="text-white bg-zinc-900">
    <div
      class="min-h-screen flex flex-col justify-center items-center space-y-6"
    >
      <NuxtLink to="/"
        ><h1 class="text-7xl font-extralight">nanos</h1></NuxtLink
      >
      <div class="px-2 w-full sm:w-4/5 md:w-3/4 lg:w-1/2 space-y-6">
        <FormCreate />
        <Nuxt />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
export default Vue.extend({
  name: 'DefaultLayout',
});
</script>
