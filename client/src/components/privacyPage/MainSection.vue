<template>
  <div v-html="text.data" class="privacy"></div>
</template>

<script>

export default {
  name: "MainSection",
  inject: [
      'backendURL',
      'frontendURL'
  ],
  props: [
    'text'
  ],
}
</script>

<style>


</style>