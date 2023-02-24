<script setup>
import { RouterLink, RouterView } from 'vue-router'
import CookieBanner from "@/components/CookieBanner.vue";
</script>

<template>
  <RouterView />
  <CookieBanner/>
</template>

<style>

body, html {
  margin: 0;
}

</style>
