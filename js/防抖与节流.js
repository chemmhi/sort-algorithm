//防抖函数
function debounce (func,time){
  let timer = null
  return function(...args){
    if(timer){
      clearTimeout(timer)
    }
    timer = setTimeout(()=>{
      func.apply(this, args)
    },time)
  }
}


//节流函数
function throttle(func, time){
  let timer = null
  return function(...args){
    if(!timer){
      timer = setTimeout(()=>{
        func.apply(this, args)
        timer = null
      },time)
    }
  }

}