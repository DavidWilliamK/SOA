import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/pages/Home'
import Authors from '@/components/pages/Authors'

Vue.use(Router)

const router = new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/home',
            name: 'home',
            component: Home
        },
        {
            path: '/authors',
            name: 'authors',
            component: Authors
        }
    ]
})

export default router