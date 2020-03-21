
// 找出数组中没有相同数值的所有数字，返回它们的个数。

func countSingle(arr: [Int]) -> Int {
    var dic: [Int: Int] = [:]
    for (idx, item) in arr.enumerated() {
        let index = dic[item]
        if index == nil {
            dic[item] = idx
        } else {
            dic.removeValue(forKey: item)
        }
    }
    return dic.keys.count
}

var arr: [Int] = [6,4,8,9,9,0,0,4,1,3,5,5,8]
print(countSingle(arr: arr))
