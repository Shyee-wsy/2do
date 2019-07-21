<template>
  <div id="app">
    <div id="list">
      <ul>
        <li v-for="item in lists" :key="item.id">{{ item.name }}</li>
        <li><input placeholder="+ 新建清单"></li>
      </ul>
    </div>
    <Item></Item>
  </div>
</template>

<script>
import Item from './Item'
export default {
  name: 'app',
  components: {
    Item
  },
  data () {
    return {
      lists:[
        {id: 0, name: 'Todo'},
        { id: 1, name: 'List1' },
        { id: 2, name: 'List2' },
        { id: 3, name: 'List3' },
        { id: 4, name: '我的计划' }
      ],
      listName: true
    }
  }
}
</script>

<style>
#app{
  width: 80vw;
  height: 100vh;
  margin: 0 auto;
}
#list{
  float: left;
  width: 20%;
  height: 100%;
  border-left: 1px solid #7e7e81;
  border-right: 1px solid #7e7e81;
  background-color: #f4f4f4;
}
*{
  box-sizing: border-box;
}
body{
  margin: 0;
}
ul li{
  border-bottom: 1px solid #7e7e81;
  list-style-type: none;
  height: 50px;
  padding: 20px;
  font-size: 20px;
}
input{
  border: none;
  padding: 5px;
  background-color: inherit;
  outline: none;
}
#list li:hover{
  font-weight: bold;
}
#list li:nth-child(1){
  margin-bottom: 20px;
}
#item ul li{
  margin-right: 30px;
  font-size: 16px;
  /*text-decoration: line-through;*/
}
li input {
  font-size: 16px;
}
</style>
