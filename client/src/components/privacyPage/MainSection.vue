<template>
  <InDevelop :frontendUrl="frontendUrl"/>
</template>

<script>
import InDevelop from "../InDevelop.vue";

export default {
  name: "MainSection",
  components: {
    InDevelop
  },
  props: [
    'backendUrl',
    'frontendUrl',
    'text'
  ],
}
</script>

<style scoped>

</style>