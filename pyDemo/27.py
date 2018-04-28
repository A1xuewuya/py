dict_info=[{"name":"nzc","age":22},
			{"name":"xwy","age":20},
			{"name":"cwy","age":10},
			{"name":"fwy","age":5}]

dict_info.sort(key=lambda x:x['name'])
print(dict_info)