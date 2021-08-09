//堆排序

const shift = function (li, low, high){
  let i = low
  let j = 2 * i + 1
  let tmp = li[i]
  while(j <= high){
    if(j < high && li[j] < li[j + 1]){
      j +=1
    }
    if(tmp < li[j]){
      li[i] = li[j]
      i = j
      j = 2 * i +1
    }else{
      break
    }
  }
  li[i] = tmp
}

const heapSort = function (li){
  let n = li.length
  //建堆
  for( let i = Math.floor(n/2) - 1; i >= 0; i--){
    shift(li, i, n-1)
  }
  //挨个出数
  for(let i = n-1; i >= 0; i--){
    let tmp = li[0]
    li[0] = li[i]
    li[i] = tmp
    shift(li, 0, i-1)
  }
  // return li
}

let a = []
for ( let i = 100000000; i > 0; i--){
  a.push(i)
}
console.log(a)
heapSort(a)
console.log(a)
