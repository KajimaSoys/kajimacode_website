<template>
<!--  <div class="image-container">-->
    <img class="in-develop-image" :src="`${frontendUrl}/src/assets/images/underDevelop_${this.$store.state.language.language}.png`" alt="Section under develop">
<!--  </div>-->
</template>

<script>
export default {
  name: "InDevelop",
  props: [
      'frontendUrl'
  ]
}
</script>

<style scoped>
/* .image-container {*/
/*     height: 100vh;*/
/*     position: absolute;*/
/*     top: 50%;*/
/*     left: 50%;*/
/*     transform: translate(-50%, -50%);*/
/*}*/
/* .image-container img{*/
/*     max-width: inherit;*/
/*     min-width: 100vw;*/
/*     height: 100vh;*/
/*}*/

 .in-develop-image {
    display: block;
    margin-left: auto;
    max-height: 70vh;
    margin-right: auto;
    padding-top: 18vh;
    padding-bottom: 18vh;
}

@media screen and (max-width: 992px) {
  .in-develop-image {
    padding-bottom: 2vh;
    max-height: 60vh;

}
}
</style>