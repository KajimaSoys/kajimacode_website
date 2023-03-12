<template>
  <div class="resume-block" id="resume">
     <div class="about-container">
       <h1 class="heading-medium">{{ text.resume_text }}</h1>

       <div class="button">
         {{ text.download_button }}
       </div>
     </div>
  </div>

</template>

<script>
export default {
  name: "ResumeSection",
  data() {
    return {

    }
  },
  props: [
    'backendUrl',
    'text'
  ],
}
</script>

<style scoped>
  .resume-block {
  padding: 0 2rem 2rem 2rem;
  max-width: 90rem;
  margin-left: auto;
  margin-right: auto;
  /*min-height: 100vh;*/
  }

  .about-container {
  text-align: justify;
  background-image: linear-gradient(235deg, #344054, #1d2939);
  border-radius: 25px;
  color: white;
  max-width: 80rem;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif;
  font-size: 1rem;
  line-height: 1.5;
  letter-spacing: normal;
  padding: 4rem;
  margin: 2rem;
}

  .heading-medium{
    color: white;
    text-align: center;
  }

  .button {
    max-width: 10rem;
    margin-left: auto;
    margin-right: auto;
    margin-top: 3rem;
    cursor: pointer;
  }
</style>