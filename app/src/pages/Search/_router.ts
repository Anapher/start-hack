import * as VueRouter from 'vue-router';

import SearchVue from './Search.vue';

const routes: VueRouter.RouteRecordRaw[] = [
  {
    path:'/search',
    name: 'Search',
    component: SearchVue
  }
];

export default routes;