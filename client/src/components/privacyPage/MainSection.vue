<template>
  <InDevelop :frontendUrl="frontendUrl"/>
<!--  <div class="fullscreen">-->
<!--    <spline-component/>-->
<!--  </div>-->
</template>

<script>
import InDevelop from "../InDevelop.vue";
import SplineComponent from "../mainPage/SplineComponent.vue";

export default {
  name: "MainSection",
  components: {
    InDevelop,
    SplineComponent
  },
  props: [
    'backendUrl',
    'frontendUrl',
    'text'
  ],
}
</script>

<style scoped>
.fullscreen {
  height: 91vh;
  margin-top: 9vh;
}
</style>