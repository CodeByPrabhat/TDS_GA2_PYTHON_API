from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔽 Embed your JSON data directly here
marks_data = [{"name":"iVItKB","marks":16},{"name":"i3sLMusPH6","marks":44},{"name":"sKioiIUqg","marks":41},{"name":"5VUDyHPfMS","marks":96},{"name":"6","marks":96},{"name":"u73S","marks":35},{"name":"WxW","marks":10},{"name":"ten","marks":62},{"name":"KhfvZA4F","marks":36},{"name":"PLjchy","marks":86},{"name":"wARJa","marks":11},{"name":"JJp4lcGN9","marks":13},{"name":"zHu3","marks":81},{"name":"tJ5NaTycK","marks":5},{"name":"kqLCKvRHid","marks":42},{"name":"9sPOKpR","marks":39},{"name":"TPGeNR","marks":19},{"name":"a","marks":89},{"name":"IZ6Z","marks":66},{"name":"gkUnXp8","marks":25},{"name":"XR","marks":73},{"name":"pgMJXmEhf","marks":75},{"name":"u","marks":59},{"name":"raqKL9oV","marks":74},{"name":"TbtDsfs2tV","marks":46},{"name":"I2D","marks":62},{"name":"TUXxpcDh","marks":79},{"name":"JM","marks":10},{"name":"kck3SX26Q8","marks":44},{"name":"Qj","marks":50},{"name":"7Btt","marks":61},{"name":"LECMFN","marks":45},{"name":"gMkbFFUFb","marks":29},{"name":"dCS8UV","marks":74},{"name":"TnEsE1","marks":83},{"name":"WTwUbe","marks":26},{"name":"DxiJCLTq","marks":10},{"name":"M","marks":34},{"name":"8VRQQ","marks":64},{"name":"ZpVkR","marks":61},{"name":"MhlOnUk","marks":52},{"name":"mO50F","marks":54},{"name":"1CpWsSx1LM","marks":10},{"name":"9AKM9JP1jv","marks":12},{"name":"89Fy","marks":26},{"name":"rr4b","marks":93},{"name":"KY","marks":7},{"name":"a31UVn","marks":83},{"name":"qpyAkaJS","marks":78},{"name":"a4uUjLZ","marks":7},{"name":"Ir","marks":83},{"name":"sBheg","marks":71},{"name":"j","marks":75},{"name":"2YO","marks":54},{"name":"CPCgRy2C","marks":28},{"name":"hjagBv","marks":20},{"name":"HdnyufWq","marks":62},{"name":"lNUtIcm","marks":53},{"name":"AZ","marks":17},{"name":"pS84I3K","marks":73},{"name":"TZ","marks":29},{"name":"f3nj5AzSVO","marks":90},{"name":"81","marks":48},{"name":"nu63ov8qjl","marks":68},{"name":"23fGgW","marks":30},{"name":"u9","marks":25},{"name":"InZ","marks":90},{"name":"9tW","marks":91},{"name":"lKOyX3Wf47","marks":28},{"name":"gDCg7eYi","marks":56},{"name":"dKRDR","marks":33},{"name":"K","marks":42},{"name":"gWhACINb","marks":79},{"name":"YDv81L","marks":61},{"name":"ASYnhQ8ha","marks":46},{"name":"Q","marks":0},{"name":"04ax","marks":16},{"name":"BqRr","marks":72},{"name":"fUD4RzKxL","marks":26},{"name":"CD","marks":78},{"name":"QO4TGRNDz","marks":1},{"name":"OYofcEa","marks":39},{"name":"1k6Ip","marks":92},{"name":"f6GEn0rJ","marks":52},{"name":"qdJHuKha","marks":17},{"name":"NQP8D8Lr","marks":49},{"name":"2W","marks":40},{"name":"2VgoRDuvNA","marks":29},{"name":"tym2t","marks":95},{"name":"P0Hkr0fJp","marks":61},{"name":"0ci","marks":22},{"name":"OkZFyen","marks":84},{"name":"57gIODa","marks":26},{"name":"JB5","marks":76},{"name":"rxsNolJ4","marks":1},{"name":"40s9sQ0","marks":8},{"name":"3EDpIlq","marks":3},{"name":"V","marks":41},{"name":"7aALUB","marks":78},{"name":"M9gzJ","marks":36}]

@app.get("/api")
def get_marks(name: list[str] = Query([])):
    name_to_marks = {str(entry["name"]): entry["marks"] for entry in marks_data}
    result = [name_to_marks.get(n, None) for n in name]
    return {"marks": result}


@app.get("/")
def root():
    return {"message": "Use /api?name=NAME to get student marks."}
