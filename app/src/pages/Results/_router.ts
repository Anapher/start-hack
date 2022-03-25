import * as VueRouter from 'vue-router';

import Results from './Results.vue';

const routes: VueRouter.RouteRecordRaw[] = [
  {
    path:'/results/:info',
    name: 'Results',
    component: Results
  }
];

export default routes;