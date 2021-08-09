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

