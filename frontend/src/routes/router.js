import { createRouter, createWebHistory } from 'vue-router';
import UserTable from '@/components/Table.vue'; 
import Profile from '@/components/Profile.vue';     

const routes = [
  {
    path: '/',
    name: 'Users',
    component: UserTable,  
  },
  
  {
    path: '/users/:username',
    name: 'UserProfile',
    component: Profile,    
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
