import Vue from 'vue'
import Router from 'vue-router'
import Logs from '@/components/Logs'
import NewItems from '@/components/NewItems'
import EditItems from '@/components/EditItems'
import ListItems from '@/components/ListItems'
import Metadata from '@/components/ListMetadata'
import NewMetadata from '@/components/NewMetadata'
import EditMetadata from '@/components/EditMetadata'
import NewCategory from '@/components/NewCategory'
import EditCategory from '@/components/EditCategory'
import Categories from '@/components/ListCategories'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [{
    path: '/',
    name: 'ListItems',
    component: ListItems
  }, {
    path: '/items/add',
    name: 'NewItems',
    component: NewItems
  }, {
    path: '/items/edit/:id',
    name: 'EditItems',
    component: EditItems
  }, {
    path: '/logs/:id',
    name: 'Logs',
    component: Logs
  }, {
    path: '/metadata',
    name: 'Metadata',
    component: Metadata
  }, {
    path: '/metadata/edit/:id',
    name: 'EditMetadata',
    component: EditMetadata
  }, {
    path: '/metadata/add',
    name: 'NewMetadata',
    component: NewMetadata
  }, {
    path: '/categories',
    name: 'Categories',
    component: Categories
  }, {
    path: '/category/add',
    name: 'NewCategory',
    component: NewCategory
  }, {
    path: '/category/edit/:id',
    name: 'EditCategory',
    component: EditCategory
  }]
})
