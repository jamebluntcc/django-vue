<template>
    <div class="home">
        <el-row display="margin-top:10px">
            <el-input v-model="input" placeholder="input book name" style="display:inline-table; width:30%; float:left"></el-input>
            <el-button type="primary" @click="addBook()" style="float: 2px;"></el-button>
        </el-row>
        <el-row>
            <el-table :data="bookList" style="width: 100%" border>
                <el-table-column prop="id" label="编号" min-width="100">
                <template scope="scope"> {{ scope.row.pk }} </template>
                </el-table-column>
                <el-table-column prop="book_name" label="书名" min-width="100">
                <template scope="scope"> {{ scope.row.fields.name }} </template>
                </el-table-column>
                <el-table-column prop="add_time" label="添加时间" min-width="100">
                <template scope="scope"> {{ scope.row.fields.create }} </template>
                </el-table-column>
            </el-table>
        </el-row>
    </div>
</template>

<script>
 export default {
     name: 'home',
     data () {
         return {
             input: '',
             bookList: []
         }
     },
     mounted: function() {
         this.showBooks()
     },
     methods: {
         addBook(){
             this.$http.get('http://127.0.0.1:8000/api/add?name=' + this.input)
                .then((response) => {
                    var res = JSON.parse(response.bodyText)
                    if (res.error_code == 0) {
                        this.showBooks()
                    } else {
                        this.$message.error('error ' + res.msg)
                    }
                })
         },
         showBooks(){
             this.$http.get('http://127.0.0.1:8000/api/books')
                .then((response) => {
                    var res = JSON.parse(response.bodyText)
                    if (res.error_code == 0){
                        this.bookList = res.books
                    } else {
                        this.$message.error('error ' + res.msg)
                    }
                })
         }
     }
 }
 </script>
<style scope>
h1, h2 {
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
</style>
