<template>
  <div v-html="text.data" class="privacy"></div>
</template>

<script>

export default {
  name: "MainSection",
  props: [
    'backendUrl',
    'frontendUrl',
    'text'
  ],
}
</script>

<style>


</style>