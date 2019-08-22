<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <div class="container">
      <table class="table table-bordered table-hover">
        <thead>
          <tr class="captionRow">
            <th colspan="9">
              <router-link class="btn btn-primary" to="/items/add">New Item</router-link>
            </th>
          </tr>
          <tr>
            <th> # </th>
            <th nowrap> Title </th>
            <th nowrap> Description </th>
            <th nowrap> Ranking </th>
            <th nowrap> Metadata </th>
            <th nowrap> Category </th>
            <th nowrap> Created On </th>
            <th nowrap> Updated On </th>
            <th nowrap> Action </th>
          </tr>
        </thead>
        <tbody>
          <tr :id="'row' + row.id" v-for="(row, index) in this.items" v-bind:key="row.id">
            <td>{{++index}}</td>
            <td>{{row.title}}</td>
            <td>{{row.description}}</td>
            <td>{{row.ranking}}</td>
            <td>{{MetadataText(row.metadata)}}</td>
            <td>{{CategoryText(row.category)}}</td>
            <td>{{row.created_date}}</td>
            <td>{{row.modified_date}}</td>
            <td nowrap>
              <router-link class="btn btn-primary" v-bind:to="'/items/edit/' + row.id">Edit</router-link>
              <button type="button" class="btn btn-danger" @click="deleteItem(row.id)">Delete</button>
              <router-link class="btn btn-info" v-bind:to="'/logs?event=Tracker&record_id=' + row.id">View Log</router-link>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import {APIService} from '../APIService'
const apiService = new APIService()

export default {
  name: 'ListItems',
  data: () => ({
    items: [],
    metadata: [],
    categories: [],
    msg: 'Favourite Items Tracker'
  }),
  mounted () {
    this.getItems()
  },
  methods: {
    getItems () {
      apiService.getData('items').then((data) => {
        this.items = data.items
      })

      apiService.getData('metadata').then((data) => {
        this.metadata = data.metadata
      })

      apiService.getData('categories').then((data) => {
        this.categories = data.categories
      })
    },
    MetadataText (pk) {
      let validMeta = this.metadata.filter((item) => {
        return item.id === pk
      })
      return validMeta[0].key
    },
    CategoryText (pk) {
      let validCategory = this.categories.filter((item) => {
        return item.id === pk
      })
      return validCategory[0].name
    },
    deleteItem (pk, ctrl) {
      apiService.deleteData('items', pk).then((data) => {
        if (data.status === 204) {
          var row = document.getElementById(`row${pk}`)
          row.parentNode.removeChild(row)
        }
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
table caption {
    line-height: 0;
    text-align: left;
}

table caption span {
    position: relative;
    left: 4px;
    top: 14px;
}

.captionRow th {
    text-align: right;
}
</style>
