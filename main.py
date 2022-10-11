from enum import Enum

from fastapi import FastAPI


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    """

    :param model_name: a name of the model_name list above
    :return:
    """
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    """
    :param file_path: a path
    :return: the path
    """
    return {"file_path": file_path}



fake_items_db = [{"item_name": "Faa"}, {"item_name": "Foo"}, {"item_name": "Fee"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    """

    :param skip: How many items to be skipped, default value : 0
    :param limit: The max number of item returned, default value : 10
    :return: some items
    """
    return fake_items_db[skip : skip + limit]


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    """
    :param item_id: the id of the item
    :param q: (OPTIONNAL) just an optional parameter, with default value : None
    :return: item_id and q if q != None
    """
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


@app.get("/items/conversion/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    """

    :param item_id: the id of the item
    :param q: (OPTIONNAL) parameter
    :param short:boolean ( accept yes / on )
    :return: a mix of the data
    """
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item