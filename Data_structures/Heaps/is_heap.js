// you may assume that the array will always have a null element at the 0-th index
function isMaxHeap(array, idx = 1) {
    if (array[idx] === undefined) return true;
    let leftIdx = idx * 2;
    let rightIdx = idx * 2 + 1;
    let leftChild = array[leftIdx] ? array[leftIdx] : -Infinity;
    let rightChild = array[rightIdx] ? array[rightIdx] : -Infinity;
    return array[idx] > leftChild && array[idx] > rightChild && isMaxHeap(array, leftIdx) && isMaxHeap(array, rightIdx);
}


module.exports = {
    isMaxHeap
};