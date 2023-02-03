import { createRouter, createWebHistory } from 'vue-router'
import MainView from '../views/MainView.vue'
import AsciiView from "../views/AsciiView.vue";
import MainViewBackup from "../views/MainViewBackup.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'main',
      component: MainView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/ascii',
      name: 'ascii',
      component: AsciiView,
    },
    {
      path: '/backup',
      name: 'backup',
      component: MainViewBackup
    }
  ],
  scrollBehavior(to, from, savedPosition) {
  if (to.hash) {
  } else if (savedPosition) {
    return savedPosition;
  } else {
    return { x: 0, y: 0 };
  }
},


})
export default router
