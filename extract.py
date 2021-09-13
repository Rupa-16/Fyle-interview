# Your imports go here
import logging
import json
logger = logging.getLogger(__name__)

'''
    Given a directory with receipt file and OCR output, this function should extract the amount

    Parameters:
    dirpath (str): directory path containing receipt and ocr output

    Returns:
    float: returns the extracted amount

'''

def extract_amount(dirpath: str) -> float:
    jsonpath=dirpath+"\ocr.json"
    file = open(jsonpath,)
    data=json.load(file)
    index=0
    output=0
    keywords=["1.00N","AMOUNT PAID","Total :","PAYMENTS","CREDIT","Total","TOTAL","TOTAL AMOUNT","Payment","Total:","Theater and Dance","PAID","Order Total","Payment via Credit Card (usina card"]
    for i in data['Blocks']:
        try:
            text=i['Text']
            # logger.info("checking %s in ===>%s",i,text)
            if text in keywords:

                # logger.info("true %s,%s",text,keywords)

                # if isinstance(data["Blocks"][index+1]["Text"],int):
                output=data["Blocks"][index+1]["Text"]
                logger.info("%s %s",text,output)
                if output == "SPRING ":
                    continue
                if output == "USD":
                    output = data["Blocks"][index + 2]["Text"]
                if output=="$":
                    output = data["Blocks"][index + 2]["Text"]
                output=output.replace("$", "")
                output = output.replace(",", "")
                output = output.replace("(", "")
                output = output.replace(")", "")
                try:
                    output=float(output);
                    logger.info('extract_amount called for dir %s ->%s->%s', dirpath, text,output)
                    break
                except ValueError:
                    print("value error")
        except KeyError:
            logger.info("e")
            # int sample=6
        index=index+1;

    # your logic goes here
    # print(dirpath)
    logger.info("returning %s",output)
    return output
