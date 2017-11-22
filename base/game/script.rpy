﻿# 您可以在此編寫遊戲的腳本。

# image命令可用於定義一個圖像。
# eg. image eileen happy = "eileen_happy.png"

# define命令可定義遊戲中出現的角色名稱與對應文本顏色。
define m = Character('瑪莉', color="#ff8c8c")
define p = Character('彼得', color="#8c8cff")
define a = Character('安娜', color="#8cff8c")
define d = Character('德比', color="#ffff8c")
define center = Character(None,
                            what_size=20,
                            what_outlines=[(3, "#000000", 0, 0)],
                            what_layout="subtitle",
                            what_xalign=0.5,
                            what_text_align=0.5,
                            window_background=None,
                            window_yminimum=0,
                            window_xfill=False,
                            window_xalign=0.5,
                            window_yalign=0.3)


# 遊戲從這裡開始。
label start:

    play music "BGM.mp3"
    scene tobecontinued

    centered "瑪莉在街上行走，在路上經過一間娃娃店，因被娃娃店的廚𥦬吸引，所以走進店內觀看，突然眼前一黑。"

    centered "第一章\n遊戲開始"
    scene s0100bgi with dissolve
    pause 0.2
    scene tobecontinued with dissolve
    pause 0.1
    scene s0100bgi with dissolve
    pause 0.5
    scene tobecontinued with dissolve
    pause 0.1
    #fade in and out for few times

    m "嗯……"
    scene s0100bgi
    m "為什麼我會在這裏的？"
    scene s0100
    m "救我……"
    scene s0101bgi
    "「咚，咚，咚……」（此時指針指向12）"
    scene s0100bgi
    show mary say
    m "終於可以動了，但為什麼會這樣？"
    show mary say at right with ease
    show peter say at left
    Character('???', color="#c8c8ff") "你是新的受害者呢......(突然聽到一把聲音)"
    show mary say at right
    show peter look at left
    m "你……是誰？"
    show peter say at left
    p "你好，我叫彼得。按你身上的名片，你叫瑪莉？"
    show mary scared at right
    m "剛剛你說什麼「新的受害者」？還有為什麼我會在這裡的？"
    show peter look at left
    p "看來你什麼都不知道呢……"

    scene tobecontinued with dissolve
    centered "第二章\n第一個朋友"
    scene s0100bgi with dissolve
    show peter say at left with dissolve
    show mary say at right with dissolve
    p "看來你什麼都不知道呢……"
    m "什麼？"
    show peter say at left
    p "你知道嗎……這裹的人偶都是用人類造成的。"
    show peter look at left
    show mary scared at right
    m "……騙人，你怎知道？"
    show peter say at left
    show mary look at right
    p "昨天我看到一個女孩，和你一模一樣的，被店主捉了，然後今天我便看到你在這裏了。這裏的人偶也一樣，你說這會是巧合麼？"
    show mary scared at right
    m "怎麼會是這樣！我是否永遠變不回去？"
    show peter say at left
    p "這裡的每一個人偶都有屬於自己的故事，十個？二十個？我都忘記至今受害者的人數，不過從未有人能解除身上的詛咒。而你......會成為改變命運的第一人嗎？"
    show mary shocked at right
    m "我想嘗試一下......"
    show peter say at left
    p "那我給你一些提示吧。你每一天只有三小時可以活動。我在尋找離開方法時，曾在收銀處前發現一些資料，這可能協助你離開這裡。"

    scene tobecontinued with dissolve
    centered "第三章\n零碎的回憶"
    scene s0300bgi with dissolve
    "（二人來到收銀處前。）"
    scene s0301bgi
    m "這本筆記是你所指的資料？"
    p "對，我在幾天前發現的，不知道有沒有離開的線索......"
    scene s0302bgi with dissolve
    m "原來是商店的資料。這裡寫「業主﹕德比」你知道這個人嗎？"
    p "他是把我們變成人偶的人......"
    scene s0100bgi
    show peter look at left
    show mary scared at right
    m "那我們最後要將他打敗，才能離開？"
    show peter say at left
    p ".......不知道....."
    m "............"
    scene s0303bgi with dissolve
    m "你看，這頁是我的購入記錄......咦？怎麼後面被撕去了一頁？"
    p "那頁寫的是身世……所有人偶的身世全被人故意撕下了。"
    scene s0100bgi
    show peter look at left
    show mary shocked at right
    m "身世會包含事情的真相嗎？"
    show peter say at left
    show mary look at right
    p "不管如何，去找找吧。我想你應該不了解店裏的結構，讓我來當嚮導吧！"
    scene s0100
    m "（這股熟悉感，我好像曾經到過這家店來，甚至不止一次？）"
    $ jump_count = 0
    $ woodBoxChoose = 0
    label reChoose1:
        scene tobecontinued with dissolve
        scene s0100bgi with dissolve
    $ jump_count += 1
    if jump_count > 5:
        scene tobecontinued with dissolve
        centered "It is the time..."
        jump badend1
    menu:
        "又到冒險的時候了，要到哪裏？"

        "木櫃":
            scene tobecontinued with dissolve
            centered "前往...\n木櫃"
            jump woodBox

        "倉庫":
            scene tobecontinued with dissolve
            centered "前往...\n倉庫"
            jump storeRoom

        "櫥窗":
            scene tobecontinued with dissolve
            centered "前往...\n櫥窗"
            jump windowLabel

    label woodBox:
        $ choiseWoodBox = "yes"
        scene s0400bgi with dissolve
        p "這櫃放的都是老古董人偶，看起來帶點古雅呢！"
        scene s0401bgi
        m "這兒......（突然眼前冒出一顆紅色圓形物件）啊！"
        scene s0100bgi
        show peter look
        p "怎麼了？"
        show peter look at left with ease
        show mary say at right
        m "沒什麼，找找筆記，我總覺得我們的身世好像在這個地方。"
        hide mary say with dissolve
        show peter say at Position(xpos=0.5, xanchor='center') with ease
        p "這三個人偶都好像有點怪怪的，搞不好其中一個就藏着我們的身世！"
        $ woodBoxChoose += 1
        scene s0400bgi with dissolve
        show opt2char1 at left with dissolve
        show opt2char2 with dissolve
        show opt2char3 at right with dissolve
        pause 3
        menu:
            "是那隻隱藏了秘密？"
            "左":
                "這只是一個已死去的普通人偶...沒有甚麼特別...斃了，店主來了！"
                jump badend1
            "中":
                "這只是一個已死去的普通人偶...沒有甚麼特別...斃了，店主來了！"
                jump badend1
            "右":
                scene tobecontinued with dissolve
                centered "你選對了，就是這顆紅色的鈕..."
                jump branch1

    label storeRoom:
        $ choiseStoreRoom = "yes"
        scene s0402bgi with dissolve
        "上了鎖的倉庫"
        "這道門開不了....."
        show peter say at left with dissolve
        p "我們先去找其他地方吧，說不定其他地方會有這門的鎖匙。"
        scene s0404bgi
        m "啊！（回想起奇怪的記憶）"
        scene tobecontinued with dissolve
        centered "回去..."
        jump reChoose1

    label windowLabel:
        scene tobecontinued with dissolve
        scene s0405bgi with dissolve
        "（二人來到櫥窗前）"
        if jump_count >= 3 and storeRoom == "yes" and  choiseStoreRoom == "yes":
            p "這裏放的都是最矚目的暢銷人偶。你可以憑記憶想起什麼暗格嗎？可能安娜就藏在這兒也說不定。"
            show mary shocked at right
            m "啊！櫥窗最頂層那個綠色箭頭標記的盒子！是我小時候用來放人偶衣服的！"
            show peter look at left
            p "它的位置太高了，我們要取點工具幫忙。"
            menu:
                "選擇哪一個？"
                "長尺":
                    "這工具不足以取得綠箱子呢...斃了，店主來了！"
                    jump badend1
                "繩子":
                    "正確答案！請繼續接受任務！"
                    jump branch2
                "人字梯":
                    "這工具笨重不足以取得綠箱子呢...斃了，店主來了！"
                    jump badend1

        p "這裏放的都是最矚目的暢銷人偶。"
        scene tobecontinued with dissolve
        centered "回去..."
        jump reChoose1

    label branch1:
        scene s0400bgi with dissolve
        m "這個人偶身上的鈕扣和剛才在我腦裏閃過的一模一樣，看！這兒有一頁紙。"
        scene s0601bgi
        "「瑪莉本為娃娃店的太子女，擁有地位崇高的父母，在別人的阿諛奉承之中並沒有任何交心的朋友，娃娃店是她的小樂園，而人偶是她唯一的玩伴。但是瑪莉因為家庭的壓力和恃寵生驕的性格，開始把人偶由玩伴變為發洩對象。」"
        show mary shocked at right
        m "娃娃店......會是這間嗎？難怪這兒對我竟有種說不出來的熟悉。"
        show peter look at left
        p "這間店真的是你的家族生意嗎？為什麼現在卻成了德比的煉獄？"
        show mary say at right
        m "噢，我想起來了，一年前一個男人提出接手經營這店，而我的爸媽不知為什麼答應了。說來奇怪，聽說這個男人開始經營娃娃店後，生意竟比之前更好，不過我從沒見過他，也已好幾年沒來這兒了。"
        show peter say at left
        show mary look at right
        p "呃，我可以向你提出一個請求嗎，瑪莉？"
        show peter look at left
        show mary say at right
        m "什麼事呢？"
        show mary look at right
        show peter say at left
        p "也許你現在就可以離開了，但你可以繼續留下替我找尋我的身世，以及安娜嗎？"
        show mary say at right
        m "安娜是誰？"
        p "她是繼我進來後的第二個受害者，是我在這兒的第一個朋友。一星期前的一晚，她說到收銀處查探一下，卻再沒回來了，我到處都找不到她，只找到那本可疑的筆記……我實在很擔心她。"
        show peter look at left
        show mary scared at right
        m "但在這個鬼地方多留一分一秒隨時身陷險境……"
        p "我明白，所以我也不想強人所難。你自己決定吧。"
        scene s0100bgi with dissolve
        menu:
            "你要怎樣做呢："
            "離開":
                scene tobecontinued with dissolve
                centered "你太天真了人類..."
                jump badend2
            "留下":
                show peter laugh with dissolve
                p "感謝你的決定！"
                show peter smile at left with ease
                show mary say at right with dissolve
                m "好吧，彼得你也是我在這兒的第一個朋友，我們一起尋找安娜吧。"
                p "謝謝你！咦，這是什麼？（指向不遠處）"
                show peter laugh at left
                m "好像是一個針線包，拿來縫補人偶用的吧？"
                p "或者之後有用也說不定，先帶着吧。"
                show peter smile at left
                m "我們下一站到哪裏？"
                show peter laugh at left
                p "不知道呢，這兒任務已完成了，回去再決定吧！"
                scene tobecontinued with dissolve
                centered "回去..."
                jump reChoose1

    label branch2:
        show mary say at right
        m "幸好繩子比長尺長，也不像人字梯那樣笨重和發出聲響，否則便可能被發現了。"
        show mary shocked at right
        show peter look at left
        p "（打開盒子）這是我的身世啊！"
        scene s0600bgi with dissolve
        "「彼得幼時愛玩玩偶，因而為人取笑，後來受朋友影響迷上了電玩。逐漸長大的彼得，開始認為男生不該玩人偶，遂將家中甚至從前最鍾愛的那個人偶都全部丟棄。」"
        show peter look at left with dissolve
        p "我是這樣貪新忘舊的人嗎？"
        show mary say at right with dissolve
        m "如果我是那個被打入冷宮的人偶，一定會心生不忿呢！"
        show peter say at left
        "（彼得白她一眼）"
        show mary scared at right
        m "開玩笑啦！"
        show mary shocked at right
        p "不好笑嘛。咦，原來盒子內還有一把鑰匙！"
        show peter look at left
        p "這......啊！是倉庫的鑰匙！"
        scene tobecontinued with dissolve
        centered "前往...\n倉庫"
        scene s0602bgi with dissolve
        p "記得你的鑰匙嗎？我們去倉庫。快用它來開倉庫的門"
        scene s0603bgi with dissolve
        pause 0.7
        scene s0604bgi with dissolve
        pause 0.7
        scene s0606bgi with dissolve
        p "想不到這裏一個人偶也沒有啊。"
        m "這裏好像特別陰森恐怖啊！我們是不是不該來這裏呢？"
        show peter say at left
        p "還是快找找提示吧，我們時間不多了。"
        scene s0607bgi
        show peter look at left
        show mary say at right
        m "這裏有五件物品啊，搞不好其中一件就藏着安娜的線索！"
        scene tobecontinued with dissolve
        scene s0605bgi with dissolve
        m "啊！（回想起奇怪的回憶）"
        # max guess 3 times
        $ jump_count = 0
        label reChoose2:
            scene tobecontinued with dissolve
            scene s0607bgi with dissolve
            $ jump_count += 1
            if jump_count > 3:
                play sound "<from 4 to 10>footSFX.mp3"
                p "有腳步聲！斃了！是店主！"
                jump badend1

        menu:
            "猜猜那件物件隱藏秘密呢？"
            "壞手提電腦":
                show mary say at right
                m "這件物件那有甚麼秘密？"
                show peter say at left
                p "不要緊繼續找吧!"
                jump reChoose2
            "藤籃":
                show mary say at right
                m "這件物件根本沒有秘密..."
                show peter say at left
                p "那真的是徒勞無功了..."
                jump reChoose2
            "補丁布袋":
                show mary say at right
                m "這件物件那有甚麼秘密？"
                show peter say at left
                p "不要緊繼續找吧!"
                jump reChoose2
            "破椅子":
                show peter say at left
                p "這件也不是了"
                show mary say at right
                m "真失望呢！"
                p "唯有找找吧！"
                show mary look at right
                m "再找不到就算了！"
                jump reChoose2
            "回收箱":
                "好像有甚麼不得了的東西在這個箱內......"
                jump recircleBin

    label recircleBin:
        scene tobecontinued with dissolve
        "（按照自己的記憶走到回收箱前）"
        show mary say with dissolve
        m "每次來到這間店時我都會到倉庫尋寶，並製造自己的秘密空間，而這個回收箱便是其中之一。但是自從自己的壓力不斷增加，這裏便變成我發洩的地方......正因為家人都不會到倉庫，所以家人並不知情，我亦持續在這裡發洩自己的不滿。我想我沒有資格對你說過份的話。"
        m "在尋找的過程中，記憶就像拼圖般一塊塊的重現我的腦海中。沒有交心朋友的我，身邊只有人偶陪伴。面對著一個不能說話的「朋友」，再加上自己的懦弱和壓力，所以利用人偶作為自己的發洩工具。"
        show mary say at right with ease
        m "我想......我會變成人偶都是理所當然的。"
        scene s0606bgi
        show mary say at right
        show peter say
        show peter say at left with ease
        p "原來如此，但是事件已經過去，你不要再責怪自己了。我們都要好好反省自己的過錯，不要再重蹈覆轍。"
        m "這我固然知道，但現在我後悔自己的所作所為，亦感到十分抱歉。"
        show mary look at right
        p "要為自己所做過的事情負責，那要等到我們離開這間店才可以贖罪。但是現在我們......"
        show mary shocked at right
        show peter look at left
        "( 聽見從回收箱中發出聲音)"
        jump chapter4

    label chapter4:
        scene tobecontinued with dissolve
        centered"第四章\n消逝的同伴"
        scene s0608bgi with dissolve
        "（二人合力爬上回收箱，赫然發現一隻破碎殘舊的人偶，奄奄一息。）"
        p "安娜！安娜！"
        m "（她便是安娜，但是怎麼會......）"
        p "安娜你為什麼會在那裏？"
        m "先救她出來再說吧！"
        scene s0609bgi with dissolve
        "（安娜的手一動，眼睛徐徐張開）"
        p "安娜！你沒事吧？"
        a "我終於等到你來到這裡，彼得。儘管在回收箱受百般折磨也沒所謂......她是......"
        show mary scared
        show mary scared at left with ease
        m "我是瑪莉。你先別說話，彼得，我想剛才的針線會幫助安娜康復。"
        scene tobecontinued with dissolve
        centered "（二人動手為安娜治療）"
        scene s0606bgi with dissolve
        show peter say at left
        p "你這段時間到哪裏去了？為什麼你會在這兒，還受了重傷？"
        show anna say at right
        a "你記得一星期前我跟你說到收銀處看看嗎？"
        show peter look at left
        p "記得。然後你便失蹤了......"
        a "當晚我在收銀處發現了筆記簿，原來上面有我們的身世。當我讀完自己的身世，我終於把所有事情記起了。彼得，你記起我了嗎？我們是老朋友啊。"
        show peter shocked at left
        p "安娜，你在說什麼？難道我們在變成人偶前就認識嗎？"
        show anna cry at right with dissolve
        a "難道你還沒恢復所有記憶嗎？關於這店的事，你還不知道？"
        show mary scared
        m "這店發生了什麼事？"
        show mary scared behind anna
        a "這是間受詛咒的娃娃店，充滿強大的怨念，來自這店的現任店主。"
        show peter scared at left
        p "德比？他究竟是誰？"
        a "故事，應該由這兒說起。（頓一頓，喘一大口氣）從前有個小男孩，一直寵愛着一個人偶，還替他取名叫「德比」。然而男孩長大後因害怕被朋友取笑自己玩玩偶，再加上迷上電玩後，將多年來陪伴身旁的德比丟棄到一旁。"
        a "被打入冷宮的德比當然很傷心，竟產生強大怨念，這股怨念足以令他能變成人類和將人類變成人偶。因被主人忽視心生歪念，向主人報復，把他變成人偶，再接手經營了一間娃娃店。"
        show anna cry behind mary
        m "德比的主人不會就是......(瞥一眼彼得)"
        p "…...為什麼我完全想不起來？"
        show mary scared behind anna
        a "因為你還未得到完整的身世。"
        scene s0610bgi with dissolve
        "（安娜慢慢的在背後取出一張合照遞給瑪莉，那是一個笑得天真爛漫的男孩抱着一個彷彿在笑的人偶。）"
        show peter shocked at left
        p "我全都想起來了！安娜，為什麼連你......"
        show peter look at left
        show anna wordless at right
        a "一年前那個黃昏，我本想為之前那場與你吵的架道歉的，剛拐到你家的後巷，便看見成為人類的德比將你變成人偶。我嚇得大叫起來，被德比發現。喪心病狂的他轉而向我下毒手，我也變成了人偶。幸運的是，我們即使成了人偶，還是做了彼此的好朋友啊，也許這是緣份吧。"
        scene s0606bgi with dissolve
        show mary shocked
        m "你怎麼會有這張合照？它不是應該跟筆記在一起嗎？"
        a "當晚我得悉事情的真相後，本想馬上拿照片回去告訴彼得，誰料德比卻出現了。他怒火中燒，一手抓住我，對我施行酷刑，再將半死不活的我丟進回收箱。幸好我早將這張重要的合照收起來。（此時倉庫外傳來腳步聲。）"
        play sound "<from 4 to 10>footSFX.mp3"
        show peter scared at left
        show anna scared at right
        show mary scared
        m "不好了！看來是德比！怎麼辦？"
        show anna say at right
        a "你們快走吧，不要花時間救我，只要彼得你平安無事，即使要我死也沒大不了！"
        show peter yell at left
        p "怎麼可以？我可不會丟下我的好朋友不顧的！"
        m "可是這樣連我們都可能逃不掉的！"
        stop sound
        menu:
            "十萬火急！應怎樣做？"
            "繼續治療安娜":
                show mary angry
                m "我不是貪生怕死的人，一定會有方法讓我們三人逃出去的！（腳步聲由遠至近，二人加緊時間治療）"
                show peter smile at left
                p "成了！"
                hide mary angry with dissolve
                show anna smile at right
                a "謝謝你。"
                show peter smile at Position(xpos=0.5, xanchor='center') with ease
                hide peter smile with dissolve
                p "安娜，小心點，不要把傷口拉開。"
                show anna smile at Position(xpos=0.5, xanchor='center') with ease
                hide anna smile with dissolve
                m "不要再浪費時間，我們盡快離開這裡。"
                p "好。"
                scene tobecontinued with dissolve
                "（兩人扶著安娜，轉頭）"
                "（砰的一聲，倉庫的門推開了。）"
                #scene tobecontinued with dissolve
                centered "第五章\n 和解、釋然"
                scene s0700 with dissolve
                d "（憤怒）你們想走！？"
                m "是店主！！！被發現了！！！"
                d "都是筆記的錯，我用了很多方法都無法燒毀筆記，這才令你們記起所有事情！那本可惡的筆記，總是自動記錄人偶的身世，自從上次被那個討厭的人偶發現後，我就一直想燒毀人偶的身世。可是只要我把它撕下來，身世便會消失得無影無踪。本以為一了百了，竟又讓你這個丫頭給找出來！"
                d "既然如此，那我把你們全都燒毀！"
                jump chapterUnknownOriginC4S5
            "離開，躲避德比":
                show mary sad
                m "彼得，安娜也不希望你有事啊！"
                show peter sad at left
                p "安娜......"
                show anna say at right
                a "我的性命並不重要，我快不行了，所以你們要仔細聆聽我的話。德比曾經是你最要好的朋友，朋友，一定要珍惜......"
                show anna think at right
                hide anna think with dissolve
                "(安娜呼出最後一口氣，再也一動不動。)"
                show peter cry at left
                show mary sad at right with ease
                p "安娜！你醒醒！"
                show mary cry at right with dissolve
                m "冷靜點彼得！安娜的心意不可以因為你一時的衝動而白費！我們趕緊尋找出路，快走吧！"
                p "德比太過分了......即使也不全是他的錯。是我連累了你們所有人，對不起，我沒資格再待在你身邊了。"
                show peter cry at Position(xpos=0.5, xanchor='center') with ease
                "（彼得打算毅然離開。）"
                "（砰的一聲，倉庫的門推開了。）"
                hide peter sad with dissolve
                show mary cry at Position(xpos=0.5, xanchor='center') with ease
                hide mary sad with dissolve
                m "無論如何，我們已找到我們的身世，不要浪費安娜的好意！趁機快走吧！"
                jump trueEnd

    label chapterUnknownOriginC4S5:
        menu:
            "應該要怎樣做呢？"
            "攻擊":
                "（德比一手抓起瑪莉，一手正想抓住彼得）"
                scene s0701 with dissolve
                m "（不可以讓朋友受傷！）"
                "（於是瑪莉伸出自己的拳頭狠狠地打在德比的手臂上。但自己是人偶的關係，力量亦變小，無法對德比造成傷害。）"
                d "你在替我抓癢嗎？"
                m "怎麼會這樣......"
                d "（奸笑）做好心理準備，你會比他們更悽慘。"
                m "（震驚）"
                p "放開瑪莉"
                scene s0702
                "（德比無視彼得的話，一手把他們都抓去。）"
                d "知道事實的真相可是要付出代價的......"
                jump badend3
            "逃走":
                scene s0606bgi with dissolve
                show mary shocked with dissolve
                m "怎麼辦？"
                show mary shocked at right with ease
                show peter say with dissolve
                p "我們的力量太小，又沒有可以作為攻擊用的工具......"
                show peter say at left with ease
                show mary shocked at Position(xpos=0.5, xanchor='center') with ease
                hide peter say
                show mary shocked at left with ease
                hide mary shocked
                m "先別想太多，現在還是先逃離德比的視線範圍吧！"
                scene s0710 with dissolve
                scene s0711 with dissolve
                "（人偶們拼命的往門跑，但忘記了他們還是個人偶，即使他們再拼命跑，德比只走幾步便能趕到他們面前，把門關掉。三人再次轉頭，但頭上響起德比的聲音）"
                scene tobecontinued with dissolve
                d "放棄吧！即使你們再努力，亦無法離開我視線範圍。你們還是死心吧！"
                scene s0700 with dissolve
                "（人偶們想逃跑，但是身後便是死路，他們逃無可逃，只能眼睜睜的望著德比的手伸過來，把自己抓住）"
                d "知道事實的真相可是要付出代價的......"
                scene tobecontinued with dissolve
                show peter scared at left with dissolve
                show mary feel bad with dissolve
                hide peter scared with dissolve
                show anna hopeless at right with dissolve
                hide mary feel bad with dissolve
                pause 0.2
                hide anna hopeless with dissolve
                "（最後的希望消失了，人偶兩眼空洞，放棄掙扎，默默的接受現實。）"
                jump badend3
            "說服":
                scene s0704 with dissolve
                "（德比正想一手抓起瑪莉，彼得上前推開她，眼裏充滿怒火的店主轉而把毒手伸向他。）"
                d "都是筆記的錯，我用了很多方法都無法燒毀筆記，這才令你們記起所有事情！"
                scene s0702
                d "既然如此，那我把你們全都燒毀！"
                m "且慢！德比，你看看這張合照，還記得嗎？"
                scene s0610bgi with dissolve
                "（德比的手一震，回想起過往與彼得的種種，那些快樂的日子。）"
                show peter cry with dissolve
                p "德比，對不起，以前是我做錯了，我不懂得好好珍惜你。是安娜提醒了我"
                hide peter cry with dissolve
                show mary cry with dissolve
                m "我也有錯，我以前也不懂得好好善待人偶，才會被你捉去。我答應你我會改過的。"
                hide mary cry with dissolve
                show keeper human sad with dissolve
                pause 0.2
                hide keeper human sad with dissolve
                d "（痛苦，不停搖頭）不會，我不會原諒你！"
                scene s0703 with dissolve
                p "（主動伸手抱着德比的手，眼泛淚光）我一定會好好改過，因為你是我最好的朋友啊，德比。"
                scene tobecontinued with dissolve
                Character('???', color="#ffff8c")  "......謝謝你們。"
                "（瑪莉和彼得立時眼前一黑，再次埋入黑暗之中。）"
                jump he

    label trueEnd:
        scene tobecontinued with dissolve
        scene he0000 with dissolve
        pause 0.2
        scene he0001 with dissolve
        pause 0.5
        scene he0002 with dissolve
        pause 0.5
        scene he0003 with dissolve
        pause 0.5
        scene he0004 with dissolve
        pause 0.5
        scene he0000 with dissolve
        center "True End-缺了一角的記憶\n\n瑪莉和彼得變回人類，但因令無辜的安娜死去，失去娃娃店的記憶，不知為甚麼對人偶有種親切的感覺。原本對人偶充滿興趣的她，卻在經過人偶店時卻對人偶產生莫名的恐懼，眼看坐在櫥窗裏的人偶，不禁同情他們。雖然感到似曾相識，但望一下後，就走開了。瑪莉走後，一個男子走來店前，望住她遠去......不知為何對這個女孩有熟悉的感覺，他不經意地舉高手輕撫店前的玻璃。"
        jump done

    label he:
        scene tobecontinued with dissolve
        scene he0100 with dissolve
        scene he0101 with dissolve
        scene he0102 with dissolve
        scene he0103 with dissolve
        pause 1
        scene he0104 with dissolve
        center "HAPPY END-邁向人生新一頁\n\n瑪莉、彼得、安娜一起逃出人偶店，變回人類，並以此為教訓，決定改過自身。瑪莉、彼得、安娜沒有忘記自己是人偶時的記憶，並記得自己如何結識朋友，幫助他逃走，明白要珍惜朋友，因為每一位朋友都是珍貴的。彼得明白自己不可貪新厭舊，他找回德比道歉，德比亦將店子轉讓給別人，德比感到很高興，然後變回人偶，從此彼得和德比一生在一起。"
        jump done

    label badend1:
        stop sound
        scene tobecontinued with dissolve
        scene ed0100 with dissolve
        center "BAD END 1-擦肩而過的真相\n\n瑪莉和彼得在尋找隱藏自己身世物件時逃脫失敗，被店主發現，瑪莉被強行放進回收箱，從此再沒見過彼得。她十分害怕，雖帶着自己是人的回憶，卻知道自己永遠動彈不得了。她似乎明白了甚麼，但只能無奈並四肢無力地等待將臨的「處置」。而店主帶着陰險的微笑尋找新的人偶。"
        jump done

    label badend2:
        scene tobecontinued with dissolve
        scene ed0200 with dissolve
        pause 1
        scene ed0201 with dissolve
        pause 1
        scene ed0202 with dissolve
        pause 1
        scene ed0203 with dissolve
        center "BAD END 2-頭腦緩慢的後果\n\n瑪莉以為得到身世後便能逃脫，誰料變回人的關鍵並非如此，一個叫瑪莉的人偶躺在門前，身體一動不動的，眼神只剩下虛空。。"
        jump done

    label badend3:
        scene tobecontinued with dissolve
        scene ed0300 with dissolve
        center "BAD END 3-觸不可及的命運\n\n知道事實的真相可是要付出代價的。人偶始終無法敵過法術強大的德比，各人迎來終結的命運。安娜、瑪莉和彼得相繼死去，而德比亦因彼得的死亡而被魔法反噬而死。肢離破碎的人偶混和血液散落一地，各人見識到前所未有的黑暗和絕望。"
        jump done

    label done:
        pass

    return
