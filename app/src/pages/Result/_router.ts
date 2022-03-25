import * as VueRouter from 'vue-router';

import Result from './Result.vue';

const routes: VueRouter.RouteRecordRaw[] = [
  {
    path:'/result',
    name: 'Result',
    component: Result
  }
];

export default routes;