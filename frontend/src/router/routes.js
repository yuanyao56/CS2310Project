
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '/', component: () => import('pages/tempType.vue') },
      { path: '/start', component: () => import('pages/tempType.vue') },
      { path: '/setTemp', component: () => import('pages/setTemp.vue') },
      { path: '/setKnob', component: () => import('pages/setKnob.vue') },
      { path: '/knob', component: () => import('pages/knob.vue') },
      { path: '/digital', component: () => import('pages/digital.vue') },
      { path: '/test', component: () => import('pages/test.vue') }

    ]
  }
]

// Always leave this as last one
if (process.env.MODE !== 'ssr') {
  routes.push({
    path: '*',
    component: () => import('pages/Error404.vue')
  })
}

export default routes
