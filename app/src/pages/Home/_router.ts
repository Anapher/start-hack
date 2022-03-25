import * as VueRouter from 'vue-router';

import Home from './Home.vue';

const routes: VueRouter.RouteRecordRaw[] = [
  {
    path:'/',
    name: 'Home',
    component: Home
  }
];

export default routes;