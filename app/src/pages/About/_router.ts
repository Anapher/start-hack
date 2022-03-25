import * as VueRouter from 'vue-router';

import About from './About.vue';

const routes: VueRouter.RouteRecordRaw[] = [
  {
    path:'/about',
    name: 'About',
    component: About
  }
];

export default routes;