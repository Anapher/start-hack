import * as VueRouter from 'vue-router';

import AboutRoutes from '../pages/About/_router';
import HomeRoutes from '../pages/Home/_router';
import SearchRouter from '../pages/Search/_router';
import ResultsRouter from '../pages/Results/_router';
import ResultRouter from '../pages/Result/_router';

const routes: VueRouter.RouteRecordRaw[] = [
  ...AboutRoutes,
  ...HomeRoutes,
  ...SearchRouter,
  ...ResultsRouter,
  ...ResultRouter
];

export const router = VueRouter.createRouter({
    history: VueRouter.createWebHistory(),
    routes,
})

router.beforeEach((to, from, next) => {
  if(typeof(to.name) === 'string'){
    document.title = to.name;
  }
  next();
});