// 二分法查找

const binSearch = function (data_set,val){
  let low = 0;
  let high = data_set.length;
  while(low<=high){
    let mid = Math.floor((low + high)/2)
    if(data_set[mid] === val){
      return mid
    }else if(data_set[mid] > val){
      high = mid -1;
    }else{
      low = mid +1
    }
  }
  return null
}

// console.log(bin_search([1,2,3,4,5,6,7,8,9],1))


//冒泡排序
const bubbuleSort = function (dataList){
  for(let i = 0; i < dataList.length-1; i++){
    for (let j = 0; j < dataList.length - i -1; j++){
      if(dataList[j]>dataList[j+1]){
        let tem = dataList[j]
        dataList[j] = dataList[j+1]
        dataList[j+1] = tem;
      }
    }
  }
  return dataList
}

// console.log(bubbuleSort([11,2,3,4,5,6,7,8,9,]))

//选择排序

const selectSort = function (data_li){
  for (let i = 0; i < data_li.length - 1; i++){
    let minPosition = i
    for (let j = i + 1; j <data_li.length; j++ ){
      if(data_li[j] < data_li[minPosition]){
        minPosition = j
      }
    }
    let tmp = data_li[i]
    data_li[i] = data_li[minPosition]
    data_li[minPosition] = tmp
  }
  return data_li
}

// console.log(selectSort([11,22,3,4,5,6,7,8,9,9.5,0]))

//插入排序

const insertSort = function (li){
  for(let i=1; i<li.length; i++){
    let tmp = li[i]
    for(let j=0; j<i;j++){
      if(tmp < li[j]){
        for(let k = i-1;k>=j;k--){
          li[k+1] = li[k]
        }
        li[j] = tmp
        break
      }
    }
  }
  return li
}

const insertSort2 = function (li){
  for(let i = 1; i < li.length; i++){
    let tmp = li[i]
    let j = i -1
    while(j >=0 && tmp<li[j]){
      li[j+1] = li[j]
      j -=1
    }
    li[j+1] = tmp;
  }
  return li
}
console.log(insertSort2([11,222,3,4,5.2,6,7,8,9,8.8,5]))