<template>
  <div data-animation="default" class="navbar07_component w-nav" data-easing2="ease" data-easing="ease" data-collapse="medium" data-w-id="2a86f3d7-e75a-cfd6-5e9f-bf6e1eddba30" role="banner" data-duration="400" id="navbar">
      <div class="navbar07_container">
        <div class="logo-container" ref="logo">
          <router-link to="/" href="/" aria-current="page" class="navbar07_logo-link w-nav-brand w--current">
            <div class="logo_component">
              <img src="src/assets/kajimacode_white_orange.svg" alt="kajimacode logo" class="logo_logotype" />
            </div>
          </router-link>
        </div>

<!--        <a ref="logo" href="/" aria-current="page" class="navbar07_logo-link w-nav-brand w&#45;&#45;current">-->
<!--         -->
<!--        </a>-->

          <nav ref="navbar" role="navigation" class="navbar07_menu w-nav-menu">
              <div class="navbar07_menu-left">
                <router-link to="/projects">
                  <a class="navbar07_link w-nav-link">Projects</a>
                </router-link>

                <router-link to="/skills">
                  <a class="navbar07_link w-nav-link">My skills</a>
                </router-link>

                <router-link to="/about">
                  <a class="navbar07_link w-nav-link">About me</a>
                </router-link>

              </div>
              <div class="navbar07_menu-right">
                <div class="navbar07_button-wrapper">
                  <a href="#" class="button-secondary-gray show-tablet w-inline-block">
                    <div>Log in</div>
                  </a>
                  <div class="w-layout-grid navbar-social-list">
                    <a href="https://www.instagram.com/kajimasoys/" target="_blank" class="navbar_social-link w-inline-block">
                      <div class="footer04_social-icon w-embed">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                          <path d="M12 2.16094C15.2063 2.16094 15.5859 2.175 16.8469 2.23125C18.0188 2.28281 18.6516 2.47969 19.0734 2.64375C19.6313 2.85938 20.0344 3.12188 20.4516 3.53906C20.8734 3.96094 21.1313 4.35938 21.3469 4.91719C21.5109 5.33906 21.7078 5.97656 21.7594 7.14375C21.8156 8.40937 21.8297 8.78906 21.8297 11.9906C21.8297 15.1969 21.8156 15.5766 21.7594 16.8375C21.7078 18.0094 21.5109 18.6422 21.3469 19.0641C21.1313 19.6219 20.8688 20.025 20.4516 20.4422C20.0297 20.8641 19.6313 21.1219 19.0734 21.3375C18.6516 21.5016 18.0141 21.6984 16.8469 21.75C15.5813 21.8063 15.2016 21.8203 12 21.8203C8.79375 21.8203 8.41406 21.8063 7.15313 21.75C5.98125 21.6984 5.34844 21.5016 4.92656 21.3375C4.36875 21.1219 3.96563 20.8594 3.54844 20.4422C3.12656 20.0203 2.86875 19.6219 2.65313 19.0641C2.48906 18.6422 2.29219 18.0047 2.24063 16.8375C2.18438 15.5719 2.17031 15.1922 2.17031 11.9906C2.17031 8.78438 2.18438 8.40469 2.24063 7.14375C2.29219 5.97187 2.48906 5.33906 2.65313 4.91719C2.86875 4.35938 3.13125 3.95625 3.54844 3.53906C3.97031 3.11719 4.36875 2.85938 4.92656 2.64375C5.34844 2.47969 5.98594 2.28281 7.15313 2.23125C8.41406 2.175 8.79375 2.16094 12 2.16094ZM12 0C8.74219 0 8.33438 0.0140625 7.05469 0.0703125C5.77969 0.126563 4.90313 0.332812 4.14375 0.628125C3.35156 0.9375 2.68125 1.34531 2.01563 2.01562C1.34531 2.68125 0.9375 3.35156 0.628125 4.13906C0.332812 4.90313 0.126563 5.775 0.0703125 7.05C0.0140625 8.33437 0 8.74219 0 12C0 15.2578 0.0140625 15.6656 0.0703125 16.9453C0.126563 18.2203 0.332812 19.0969 0.628125 19.8563C0.9375 20.6484 1.34531 21.3188 2.01563 21.9844C2.68125 22.65 3.35156 23.0625 4.13906 23.3672C4.90313 23.6625 5.775 23.8687 7.05 23.925C8.32969 23.9812 8.7375 23.9953 11.9953 23.9953C15.2531 23.9953 15.6609 23.9812 16.9406 23.925C18.2156 23.8687 19.0922 23.6625 19.8516 23.3672C20.6391 23.0625 21.3094 22.65 21.975 21.9844C22.6406 21.3188 23.0531 20.6484 23.3578 19.8609C23.6531 19.0969 23.8594 18.225 23.9156 16.95C23.9719 15.6703 23.9859 15.2625 23.9859 12.0047C23.9859 8.74688 23.9719 8.33906 23.9156 7.05938C23.8594 5.78438 23.6531 4.90781 23.3578 4.14844C23.0625 3.35156 22.6547 2.68125 21.9844 2.01562C21.3188 1.35 20.6484 0.9375 19.8609 0.632812C19.0969 0.3375 18.225 0.13125 16.95 0.075C15.6656 0.0140625 15.2578 0 12 0Z" fill="currentColor" />
                          <path d="M12 5.83594C8.59688 5.83594 5.83594 8.59688 5.83594 12C5.83594 15.4031 8.59688 18.1641 12 18.1641C15.4031 18.1641 18.1641 15.4031 18.1641 12C18.1641 8.59688 15.4031 5.83594 12 5.83594ZM12 15.9984C9.79219 15.9984 8.00156 14.2078 8.00156 12C8.00156 9.79219 9.79219 8.00156 12 8.00156C14.2078 8.00156 15.9984 9.79219 15.9984 12C15.9984 14.2078 14.2078 15.9984 12 15.9984Z" fill="currentColor" />
                          <path d="M19.8469 5.59214C19.8469 6.38902 19.2 7.0312 18.4078 7.0312C17.6109 7.0312 16.9688 6.38433 16.9688 5.59214C16.9688 4.79526 17.6156 4.15308 18.4078 4.15308C19.2 4.15308 19.8469 4.79995 19.8469 5.59214Z" fill="currentColor" />
                        </svg>
                      </div>
                    </a>
                    <a href="https://github.com/KajimaSoys" class="navbar_social-link w-inline-block" target="_blank">
                      <div class="footer04_social-icon w-embed">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none">
                          <path d="M12,0a12.11,12.11,0,0,0-3.8,23.58c.6.12.82-.26.82-.58s0-1.25,0-2.25c-3.34.72-4-1.44-4-1.44a3.11,3.11,0,0,0-1.33-1.76c-1.09-.74.08-.74.08-.74a2.53,2.53,0,0,1,1.85,1.24,2.55,2.55,0,0,0,3.5,1,2.56,2.56,0,0,1,.75-1.62c-2.66-.28-5.47-1.32-5.47-6A4.74,4.74,0,0,1,5.59,8.21,4.36,4.36,0,0,1,5.71,5s1-.32,3.3,1.24a11.29,11.29,0,0,1,3-.4,11.54,11.54,0,0,1,3,.4C17.3,4.69,18.31,5,18.31,5a4.36,4.36,0,0,1,.12,3.2,4.65,4.65,0,0,1,1.24,3.25c0,4.65-2.81,5.67-5.49,6A2.89,2.89,0,0,1,15,19.67c0,1.62,0,2.93,0,3.33s.22.7.82.58A12.11,12.11,0,0,0,12,0Z" fill="currentColor"/>
                        </svg>
                      </div>
                    </a>
                    <a href="https://www.linkedin.com/in/vadim-grishin-95b70a193/" class="navbar_social-link w-inline-block" target="_blank">
                      <div class="footer04_social-icon w-embed">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                          <path d="M22.2234 0H1.77187C0.792187 0 0 0.773438 0 1.72969V22.2656C0 23.2219 0.792187 24 1.77187 24H22.2234C23.2031 24 24 23.2219 24 22.2703V1.72969C24 0.773438 23.2031 0 22.2234 0ZM7.12031 20.4516H3.55781V8.99531H7.12031V20.4516ZM5.33906 7.43438C4.19531 7.43438 3.27188 6.51094 3.27188 5.37187C3.27188 4.23281 4.19531 3.30937 5.33906 3.30937C6.47813 3.30937 7.40156 4.23281 7.40156 5.37187C7.40156 6.50625 6.47813 7.43438 5.33906 7.43438ZM20.4516 20.4516H16.8937V14.8828C16.8937 13.5562 16.8703 11.8453 15.0422 11.8453C13.1906 11.8453 12.9094 13.2937 12.9094 14.7891V20.4516H9.35625V8.99531H12.7687V10.5609H12.8156C13.2891 9.66094 14.4516 8.70938 16.1813 8.70938C19.7859 8.70938 20.4516 11.0813 20.4516 14.1656V20.4516Z" fill="currentColor" />
                        </svg>
                      </div>
                    </a>
                  </div>
                  <a href="https://t.me/OneDudeAdam" target="_blank" class="button w-inline-block">
                    <div class="text-block-4">Message in Telegram</div>
                  </a>
                </div>
              </div>
            </nav>

        <div class="w-nav-overlay" ref="overlay"></div>


        <input type="checkbox"  id="menu">
        <label for="menu" class="icon" @click="openMenu">
                <div class="menu"></div>
         </label>
      </div>
    </div>

</template>

<script>
export default {
  name: "Navbar",
  data(){
    return {
      menu: false,
      changedToDefault: false,
      changedToSmall: false,

      width: document.documentElement.clientWidth,
      height: document.documentElement.clientHeight
    }
  },
  mounted() {
    if (this.width > 991){
      this.changedToDefault = true
    } else {
      this.changedToSmall = true
      this.$refs.overlay.style.display = 'block'
      this.$refs.overlay.appendChild(this.$refs.navbar)

      this.$refs.navbar.style.display = 'block'

      this.$refs.navbar.style.transform = 'translateY(-100vh) translateX(0px)'
      this.$refs.navbar.style.transition = 'transform 400ms ease 0s'
    }

    window.addEventListener('resize', this.getDimensions);


  },

  unmounted() {
    window.removeEventListener('resize', this.getDimensions);
  },

  methods: {
    openMenu(){
      if (!this.menu){
        this.$refs.navbar.style.transform = 'translateY(0px) translateX(0px)'

        this.menu = true
      } else {
        this.$refs.navbar.style.transform = 'translateY(-100vh) translateX(0px)'

        this.menu = false
      }
    },

    getDimensions() {
      this.width = document.documentElement.clientWidth;
      this.height = document.documentElement.clientHeight;

      this.checkWidth()
    },

    checkWidth(){
      if (this.width > 991){
        if (!this.changedToDefault){
          this.$refs.logo.after(this.$refs.navbar)
          this.$refs.navbar.style.transform = 'translateY(0px) translateX(0px)'
          this.$refs.navbar.style.display = 'flex'


          this.changedToDefault = !this.changedToDefault
          this.changedToSmall = !this.changedToSmall
        }
      } else {
        if(!this.changedToSmall){
          this.$refs.overlay.style.display = 'block'
          this.$refs.overlay.appendChild(this.$refs.navbar)

          this.$refs.navbar.style.display = 'block'

          this.$refs.navbar.style.transform = 'translateY(-100vh) translateX(0px)'
          this.$refs.navbar.style.transition = 'transform 400ms ease 0s'


          this.changedToSmall = !this.changedToSmall
          this.changedToDefault = !this.changedToDefault
        }
      }

    }
  }

}
</script>

<style>

input#menu, label.icon {
  visibility: hidden;
}

.navbar_social-link {
  color: #cdd1d8;
  transition: all 300ms ease;
}

.navbar_social-link:hover{
  color: #ffffff;
}



@media screen and (max-width: 991px) {
  input#menu, label.icon {
    visibility: visible;
  }


  input#menu {
      display: none;
  }

  .icon {
    cursor: pointer;
    display: block;
    height: 24px;
    padding: 20px;
    width: 24px;
  }

  label.icon {
    position: relative;
    z-index: 200;
    padding-right: 5%;
    padding-bottom: 30px
  }

  .icon .menu,
  .icon .menu::before,
  .icon .menu::after {
    background: #4c5460;
    content: '';
    display: block;
    height: 2px;
    position: absolute;
    transition: background ease .3s, top ease .3s .3s, transform ease .3s;
    width: 20px;
  }

  .icon:hover .menu,
  .icon:hover .menu::before,
  .icon:hover .menu::after {
    background: #ff5f29;
  }

  .icon .menu {
    left: 18px;
    top: 27px;
  }

  .icon .menu::before {
    top: -6px;
  }

  .icon .menu::after {
    top: 6px;
  }

  #menu:checked + .icon .menu {
    background: transparent;
  }

  #menu:checked + .icon .menu::before {
    transform: rotate(45deg);
  }

  #menu:checked + .icon .menu::after {
    transform: rotate(-45deg);
  }

  #menu:checked + .icon .menu::before,
  #menu:checked + .icon .menu::after {
    top: 0;
    transition: top ease .3s, transform ease .3s .3s;
  }

  .w-nav-overlay{
    height: 91vh;
  }

  .navbar07_menu {
    width: 100%;
  }

  .navbar07_menu-left{
    width: 100%;
  }

  .navbar_social-link {
    color: #98a2b3;
    transition: all 300ms ease;
  }

  .navbar_social-link:hover{
    color: #667085;
  }

  .footer04_social-icon > img  {
    max-width: inherit;
  }
}
</style>