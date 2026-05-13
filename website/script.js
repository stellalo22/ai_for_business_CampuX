const { initialListings, initialWantedPosts, STORAGE_KEY, LANGUAGE_KEY } = window.marketData;

const uiText = {
  en: {
    studentVerified: "Student Verified",
    menu: "Menu",
    closeMenu: "Close",
    login: "Log in",
    myHub: "My",
    messages: "Messages",
    orders: "My Orders",
    viewCart: "View Cart",
    cartShort: "Cart",
    cartItemsCount: "items",
    jumpToSell: "Sell an Item",
    heroTag: "Buy smarter. Sell faster. Keep value on campus.",
    heroTitle: "The trusted second-hand marketplace for campus life.",
    heroDescription:
      "Discover books, digital devices, lifestyle essentials and fashion items from verified students. Search by course code, semester or category, and list your own items in under a minute.",
    exploreNow: "Explore Listings",
    joinNow: "Join Campus Market",
    modeBrowse: "Browse Items",
    modeSell: "Sell an Item",
    modeWanted: "Post Wanted",
    secureTitle: "Secure marketplace",
    secureDesc: "Verified campus identities, moderated content and protected meet-up guidance.",
    smartTitle: "Smart search",
    smartDesc: "Find items by keyword, course code, professor, semester or budget.",
    aiAssistTitle: "AI selling assistant",
    aiAssistDesc: "Generate polished titles, better descriptions and pricing suggestions.",
    campusExperience: "Campus Experience",
    campusHeadline: "Designed like a real student product, not a project slide",
    campusDesc:
      "Discover, compare, message and meet on campus in a flow that feels familiar, fast and student-first.",
    journeyTitle1: "Find what matches your semester",
    journeyDesc1:
      "Search by course code, category or budget and surface listings that are actually relevant to student life.",
    journeyTitle2: "Check details before you commit",
    journeyDesc2:
      "Open a dedicated item page, compare condition, tags, seller profile and available pickup spots.",
    journeyTitle3: "Message and meet safely on campus",
    journeyDesc3:
      "Move into chat, confirm price and plan a handoff near familiar campus pickup spots.",
    galleryEyebrow: "Campus mood",
    galleryTitle: "Built around the places students already know",
    galleryDesc:
      "Library steps, dorm lobbies and teaching buildings become natural pickup anchors.",
    galleryBadge: "Verified campus-only exchange",
    whyUseTitle: "Why students would actually use this",
    whyUse1Title: "Fast listing flow",
    whyUse1Desc: "Post in under a minute with AI-assisted wording and campus-friendly tags.",
    whyUse2Title: "Trust at a glance",
    whyUse2Desc: "Verified student identity, pickup zones and clean seller ratings reduce friction.",
    whyUse3Title: "Detail-first shopping",
    whyUse3Desc: "Dedicated product pages make it easier to compare value before opening chat.",
    whyUse4Title: "Conversation built in",
    whyUse4Desc: "Messaging feels like the natural next step instead of pushing users off-platform.",
    quickEntryTitle: "Quick entry points",
    quick1Title: "Account",
    quick1Desc: "Log in or sign up",
    quick2Title: "Item page",
    quick2Desc: "See a product detail view",
    quick3Title: "Messages",
    quick3Desc: "Open the buyer-seller chat flow",
    quick4Title: "Seller form",
    quick4Desc: "Post a new campus listing",
    marketplaceEyebrow: "Marketplace",
    marketplaceTitle: "Browse campus listings",
    marketplaceDesc:
      "Search, save, buy, or post in a few taps!",
    wantedEyebrow: "Wanted Board",
    wantedTitle: "Post what you want to buy",
    wantedDesc: "Not every need starts from browsing. Post a wanted request so sellers know what you are looking for.",
    wantedItem: "Wanted item",
    wantedBudget: "Budget (RMB)",
    wantedBuyer: "Your name",
    wantedLocation: "Preferred pickup point",
    wantedDetails: "Wanted details",
    wantedPublish: "Post Wanted",
    wantedPlaceholder: "iClicker / mini fridge / finance textbook",
    wantedDescriptionPlaceholder: "Describe condition, edition, budget flexibility or urgency...",
    wantedInitial: "Post a clear wanted request so sellers can contact you faster.",
    wantedPublished: "Wanted request posted. It is now visible in the wanted board.",
    wantedTag: "Wanted",
    budgetLabel: "Budget",
    searchLabel: "Search",
    searchPlaceholder: "Search by item, course code, seller...",
    categoryLabel: "Category",
    allCategories: "All categories",
    conditionLabel: "Condition",
    allConditions: "All conditions",
    likeNew: "Brand New",
    good: "Light Signs of Use",
    fair: "Visible Signs of Use",
    worn: "Stained",
    sortLabel: "Sort",
    recommended: "Recommended",
    lowToHigh: "Price: Low to High",
    highToLow: "Price: High to Low",
    sellerRating: "Seller rating",
    maxPrice: "Maximum price:",
    campusFiltersTitle: "Campus filters",
    campusFilter1: "Student-only verified listings",
    campusFilter2: "Course and semester tags",
    campusFilter3: "Pick-up friendly locations",
    favorites: "Favorites",
    showingFavorites: "Showing Favorites",
    reset: "Reset",
    listings: "listings",
    listing: "listing",
    cartEyebrow: "Cart",
    cartTitle: "Your picks",
    total: "Total",
    proceedCheckout: "Proceed to Checkout",
    checkoutEyebrow: "Checkout",
    checkoutTitle: "Confirm your campus pickup order",
    checkoutLead: "Review selected items, leave your contact details and continue to the handoff confirmation flow.",
    checkoutName: "Full Name",
    checkoutPhone: "Phone / WeChat",
    checkoutPickupPoint: "Pickup Location",
    checkoutTime: "Preferred Time",
    checkoutMessage: "Message to Seller",
    checkoutConfirm: "Confirm Order",
    checkoutSummary: "Order Summary",
    checkoutItems: "Items",
    checkoutPageHint: "Orders stay inside CampuX until pickup details are confirmed.",
    checkoutSuccess: "Order confirmed. The seller can now review your pickup request inside CampuX.",
    checkoutSuccessEyebrow: "Order Confirmed",
    checkoutSuccessTitle: "Your pickup request has been submitted",
    checkoutOrderId: "Order ID",
    checkoutContinue: "Continue Browsing",
    ordersEyebrow: "My Orders",
    ordersTitle: "Track your campus pickup requests",
    ordersLead: "Review submitted orders, pickup plans and seller follow-up in one place.",
    ordersSummary: "Order Snapshot",
    ordersCount: "Orders",
    ordersLatest: "Latest",
    ordersEmpty: "No orders yet. Add items to cart and complete checkout to see them here.",
    ordersStatus: "Pending seller reply",
    cartHint: "Reserve items for a campus handoff or payment flow.",
    dmEyebrow: "Direct message",
    dmTitle: "Seller inbox preview",
    sellEyebrow: "Seller Studio",
    sellTitle: "Post a new listing",
    sellDesc:
      "This demo form adds your item directly to the listing board and applies a polished English presentation automatically.",
    itemTitle: "Item title",
    imageUpload: "Item Photo",
    imageUploadHint: "Upload an image or take a photo of your item.",
    category: "Category",
    price: "Price (RMB)",
    condition: "Condition",
    sellerName: "Seller name",
    pickupPoint: "Pick-up point",
    description: "Description",
    titlePlaceholder: "Macroeconomics textbook set",
    sellerPlaceholder: "Your English name",
    locationPlaceholder: "TA building lobby",
    descriptionPlaceholder: "Add details, course tags, included accessories, availability...",
    chooseCategory: "Choose a category",
    textbooks: "Books & Study Materials",
    electronics: "Digital & Electronics",
    dormEssentials: "Lifestyle Essentials",
    fashion: "Fashion & Bags",
    chooseCondition: "Choose condition",
    generateAi: "Generate AI Description",
    publish: "Publish Listing",
    aiEyebrow: "AI layer",
    aiTitle: "What the assistant can do",
    ai1: "Suggest a clearer English title for campus buyers",
    ai2: "Recommend a fair student-friendly price",
    ai3: "Highlight tags like course code, semester and bundle value",
    ai4: "Flag risky words before the listing goes live",
    aiInitial:
      "Start with a title and category, then use the AI button to draft a better listing description.",
    emptyListings: "No listings match your current filters. Try widening the search.",
    emptyCart: "Your cart is empty. Add something you want to reserve.",
    addItemsFirst: "Add items first, then continue to the checkout flow.",
    checkoutReady:
      "Checkout is ready. In a production version, this would connect to payment and order confirmation.",
    aiNeedInput: "Please add at least an item title and category so the AI draft can sound specific.",
    aiGenerated:
      "AI draft generated. You can now edit the wording, add course codes or mention accessories before publishing.",
    published: "Listing published. It has been added to the marketplace above.",
    remove: "Remove",
    deleteListing: "Delete",
    qty: "Qty",
    ratingSuffix: "/ 5 rating",
    addToCart: "Add to cart",
    details: "Details",
    defaultAiPrice: "a fair student rate",
    newListing: "New Listing",
    studentPost: "Student Post",
    fresh: "Fresh",
    campusDeal: "Campus Deal",
    authEyebrow: "Student Access",
    authTitle: "Join the CampuX second-hand community",
    authLead: "Use your campus identity to buy, sell and message with confidence on CampuX.",
    loginTab: "Log In",
    registerTab: "Create Account",
    email: "Email",
    password: "Password",
    studentId: "Student ID",
    loginSubmit: "Continue to dashboard",
    fullName: "Full name",
    college: "College / Program",
    campusEmail: "Campus email",
    createPassword: "Create password",
    pickupPreference: "Preferred pickup zone",
    registerSubmit: "Create student account",
    authNote: "Demo only: submitting will take you back into the marketplace flow.",
    backToMarketplace: "← Back to marketplace",
    detailEyebrow: "Campus listing",
    pickup: "Pickup",
    offer: "Make an offer",
    seller: "Seller",
    sellerNote: "Usually replies within a few hours and prefers on-campus handoff.",
    tags: "Tags",
    chat: "Chat with seller",
    inbox: "Inbox",
    conversations: "Your conversations",
    activeThread: "Active thread",
    message: "Message",
    composerPlaceholder: "Type a message to confirm price or pickup...",
    send: "Send",
    copy: "Copy",
    copied: "Copied",
    recall: "Recall",
    recallExpired: "Recall unavailable",
    recalledMessage: "Message recalled",
    snippetText1: "Meet outside library at 6:30 PM?",
    snippetText2: "I can bundle the calculator...",
    strategyEyebrow: "Platform Strategy",
    strategyTitle: "From campus trading tool to AI-powered commerce hub",
    strategyDesc:
      "This concept combines student-to-student resale, merchant advertising, verified trust, and AI-assisted operations in one focused campus product.",
    flowTitle1: "Verified users enter",
    flowDesc1: "Students, advertisers, tutors, recruiters and nearby merchants join with role-based access.",
    flowTitle2: "Items or ads are created",
    flowDesc2: "Physical goods, digital services, job posts and sponsored campaigns all enter structured flows.",
    flowTitle3: "AI improves quality",
    flowDesc3: "AI helps with copy, pricing, review, matching, first-response customer service and push targeting.",
    flowTitle4: "Meetup and follow-up",
    flowDesc4: "Users coordinate time and location, receive reminders, complete the handoff, and leave ratings.",
    layerTitle1: "User Layer",
    layerDesc1: "Buyers, sellers, advertisers and admins share one identity and credit framework built on campus verification.",
    layerTitle2: "Gateway Layer",
    layerDesc2: "API gateway, H5 client, mini-app entry and notification channels route every request safely into the platform.",
    layerTitle3: "Core Business",
    layerDesc3: "Listings, transactions, user center, ad system, ratings, compliance and payment escrow form the product core.",
    layerTitle4: "AI Capability",
    layerDesc4: "AI fill-in, pricing review, matching engine and RAG support reduce friction while improving trust and efficiency.",
    layerTitle5: "Infrastructure",
    layerDesc5: "MySQL, Redis, object storage, message queues and analytics keep the platform responsive, traceable and scalable.",
    bizTitle1: "Value Proposition",
    bizList1: [
      "Centralized campus marketplace that removes repeated posting and fragmented searching.",
      "AI-assisted listing, review, pricing and communication reduce time cost on both sides.",
      "Verified trust, ratings and structured meetup flow make transactions feel safer and clearer.",
    ],
    bizTitle2: "Revenue Stream",
    bizList2: [
      "Advertising fees from local merchants, recruiters, agencies and service providers.",
      "Paid boosting for urgent sellers who want more visibility.",
      "Featured placement and premium campaign tools for campus-facing businesses.",
      "Optional deposit and escrow-related service fees for higher-trust transactions.",
    ],
    bizTitle3: "Exclusive Benefit",
    bizList3: [
      "Saves time by concentrating listings, conversations and decision-making in one place.",
      "Improves accuracy with AI-generated copy, condition review, pricing reference and targeted matching.",
      "Breaks response-time barriers with AI-assisted first replies for merchants and advertisers.",
    ],
  },
  zh: {
    studentVerified: "学生认证",
    menu: "菜单",
    closeMenu: "收起",
    login: "登录",
    myHub: "我的",
    messages: "消息",
    orders: "我的订单",
    viewCart: "查看购物车",
    cartShort: "购物车",
    cartItemsCount: "件商品",
    jumpToSell: "发布商品",
    heroTag: "更轻松地买卖，让价值继续在校园流动。",
    heroTitle: "面向港中深社区的可信校园二手交易平台。",
    heroDescription:
      "浏览教材资料、数码电子、生活用品和服饰鞋包类商品。支持按课程号、学期和分类搜索，认证学生可以快速发布自己的闲置物品。",
    exploreNow: "浏览商品",
    joinNow: "加入校园市场",
    modeBrowse: "浏览商品",
    modeSell: "发布商品",
    modeWanted: "发布求购",
    secureTitle: "安全交易",
    secureDesc: "支持校园身份认证、内容审核和线下交接提醒。",
    smartTitle: "智能搜索",
    smartDesc: "可按关键词、课程号、教授、学期或预算筛选商品。",
    aiAssistTitle: "AI 发布助手",
    aiAssistDesc: "帮助生成更自然的标题、描述和价格建议。",
    campusExperience: "校园体验",
    campusHeadline: "更像真实学生产品，而不是汇报型页面",
    campusDesc: "从搜索、查看详情、发消息到线下交接，整个流程都围绕学生真实使用习惯设计。",
    journeyTitle1: "先找到和你学期相关的商品",
    journeyDesc1: "按课程号、分类或预算搜索，更快看到真正和学生生活相关的内容。",
    journeyTitle2: "下决定前先看清细节",
    journeyDesc2: "进入独立商品详情页，比较成色、标签、卖家信息和可交接地点。",
    journeyTitle3: "再发消息确认并校内交接",
    journeyDesc3: "直接进入聊天页面，确认价格和时间，在熟悉的港中深地点完成交易。",
    galleryEyebrow: "校园氛围",
    galleryTitle: "围绕学生熟悉的校园场景来设计",
    galleryDesc: "图书馆、宿舍大堂和教学楼都可以成为自然的交接地点。",
    galleryBadge: "仅限校园认证用户交易",
    whyUseTitle: "为什么学生会愿意真的使用它",
    whyUse1Title: "发布更快",
    whyUse1Desc: "借助 AI 文案和校园标签，1 分钟内就能完成商品发布。",
    whyUse2Title: "信任更清晰",
    whyUse2Desc: "学生认证、交接地点和卖家评分能明显降低沟通成本。",
    whyUse3Title: "先看详情再决定",
    whyUse3Desc: "独立商品详情页让买家更容易判断值不值得，再决定是否发消息。",
    whyUse4Title: "聊天就是自然下一步",
    whyUse4Desc: "不用跳到别的平台，站内就能继续沟通和推进交易。",
    quickEntryTitle: "快速入口",
    quick1Title: "账号页面",
    quick1Desc: "登录或注册",
    quick2Title: "商品详情",
    quick2Desc: "查看完整商品页",
    quick3Title: "聊天消息",
    quick3Desc: "打开买卖双方聊天流程",
    quick4Title: "卖家发布",
    quick4Desc: "快速发布新商品",
    marketplaceEyebrow: "交易市场",
    marketplaceTitle: "浏览校园商品",
    marketplaceDesc:
      "先搜一搜，喜欢的先收藏，想买就加购物车，想卖就直接发布！",
    wantedEyebrow: "收物广场",
    wantedTitle: "发布你想收的东西",
    wantedDesc: "不是所有需求都要靠刷商品。先发求购，让卖家知道你正在找什么。",
    wantedItem: "想收的物品",
    wantedBudget: "预算（元）",
    wantedBuyer: "你的姓名",
    wantedLocation: "希望交接地点",
    wantedDetails: "求购说明",
    wantedPublish: "发布求购",
    wantedPlaceholder: "例如：iClicker / 小冰箱 / 金融教材",
    wantedDescriptionPlaceholder: "补充品相要求、版本要求、预算浮动空间或是否急收...",
    wantedInitial: "把需求写清楚，卖家更容易主动联系你。",
    wantedPublished: "求购信息已发布，已显示在上方收物广场。",
    wantedTag: "求购中",
    budgetLabel: "预算",
    searchLabel: "搜索",
    searchPlaceholder: "按商品、课程号、卖家搜索...",
    categoryLabel: "分类",
    allCategories: "全部分类",
    conditionLabel: "成色",
    allConditions: "全部成色",
    likeNew: "全新",
    good: "轻微使用痕迹",
    fair: "明显使用痕迹",
    worn: "污损",
    sortLabel: "排序",
    recommended: "推荐优先",
    lowToHigh: "价格从低到高",
    highToLow: "价格从高到低",
    sellerRating: "卖家评分",
    maxPrice: "最高价格：",
    campusFiltersTitle: "校园筛选",
    campusFilter1: "仅显示学生认证商品",
    campusFilter2: "支持课程和学期标签",
    campusFilter3: "方便校内当面交接",
    favorites: "收藏",
    showingFavorites: "仅看收藏",
    reset: "重置",
    listings: "个商品",
    listing: "个商品",
    cartEyebrow: "购物车",
    cartTitle: "你的选择",
    total: "合计",
    proceedCheckout: "前往结算",
    checkoutEyebrow: "结算",
    checkoutTitle: "确认你的校内交接订单",
    checkoutLead: "检查已选商品，填写联系方式和交接偏好，然后进入订单确认流程。",
    checkoutName: "姓名",
    checkoutPhone: "电话 / 微信",
    checkoutPickupPoint: "交接地点",
    checkoutTime: "希望时间",
    checkoutMessage: "给卖家的留言",
    checkoutConfirm: "确认下单",
    checkoutSummary: "订单摘要",
    checkoutItems: "商品数量",
    checkoutPageHint: "订单会先保留在 CampuX 内，直到双方确认交接细节。",
    checkoutSuccess: "订单已确认，卖家现在可以在 CampuX 内看到你的交接请求。",
    checkoutSuccessEyebrow: "订单已确认",
    checkoutSuccessTitle: "你的交接请求已经提交",
    checkoutOrderId: "订单编号",
    checkoutContinue: "继续浏览",
    ordersEyebrow: "我的订单",
    ordersTitle: "查看你的校内交接订单",
    ordersLead: "在这里查看已提交订单、交接安排和卖家后续回复。",
    ordersSummary: "订单概览",
    ordersCount: "订单数量",
    ordersLatest: "最新订单",
    ordersEmpty: "你还没有订单。先加入购物车并完成结算，订单就会显示在这里。",
    ordersStatus: "等待卖家回复",
    cartHint: "你可以先保留心仪商品，再线下当面交易或接入支付流程。",
    dmEyebrow: "私信",
    dmTitle: "卖家消息预览",
    sellEyebrow: "卖家工作台",
    sellTitle: "发布新商品",
    sellDesc: "这个演示表单会把你的商品直接加入上方列表，并自动生成更自然的商品文案。",
    itemTitle: "商品标题",
    imageUpload: "商品图片",
    imageUploadHint: "可以直接上传图片，也支持手机直接拍摄商品。",
    category: "分类",
    price: "价格（元）",
    condition: "成色",
    sellerName: "卖家姓名",
    pickupPoint: "交接地点",
    description: "商品描述",
    titlePlaceholder: "例如：宏观经济学教材套装",
    sellerPlaceholder: "你的姓名",
    locationPlaceholder: "例如：TA 教学楼大堂",
    descriptionPlaceholder: "补充商品细节、课程标签、配件、可交易时间等...",
    chooseCategory: "选择分类",
    textbooks: "教材资料",
    electronics: "数码电子",
    dormEssentials: "生活用品",
    fashion: "服饰鞋包",
    chooseCondition: "选择成色",
    generateAi: "AI 生成描述",
    publish: "发布商品",
    aiEyebrow: "AI 助手",
    aiTitle: "AI 助手可以做什么",
    ai1: "把标题改得更清晰、更适合校园买家",
    ai2: "给出更合理的学生友好定价建议",
    ai3: "突出课程号、学期和套装价值",
    ai4: "在发布前提醒风险词和敏感表达",
    aiInitial: "先填写标题和分类，再点击 AI 按钮生成更完整的商品描述。",
    emptyListings: "当前筛选条件下没有商品，可以试着放宽搜索范围。",
    emptyCart: "购物车还是空的，先加入一些想要的商品吧。",
    addItemsFirst: "请先加入商品，再继续结算。",
    checkoutReady: "已准备进入结算流程。正式版本中这里可以接支付和订单确认。",
    aiNeedInput: "请至少填写商品标题和分类，这样生成的描述才会更准确。",
    aiGenerated: "AI 描述已生成。你可以继续补充课程号、配件和交易细节后再发布。",
    published: "商品已发布，并已加入上方的商品列表。",
    remove: "删除",
    deleteListing: "删除",
    qty: "数量",
    ratingSuffix: "/ 5 分",
    addToCart: "加入购物车",
    details: "查看详情",
    defaultAiPrice: "友好价格",
    newListing: "新发布",
    studentPost: "学生发布",
    fresh: "最新",
    campusDeal: "校园好价",
    authEyebrow: "学生入口",
    authTitle: "加入港中深校园二手社区",
    authLead: "通过校园身份进入，更安心地买卖和沟通。",
    loginTab: "登录",
    registerTab: "注册账号",
    email: "邮箱",
    password: "密码",
    studentId: "学号",
    loginSubmit: "进入市场",
    fullName: "姓名",
    college: "书院 / 专业",
    campusEmail: "校园邮箱",
    createPassword: "设置密码",
    pickupPreference: "常用交接地点",
    registerSubmit: "创建学生账号",
    authNote: "这是演示页面：提交后会回到首页继续浏览流程。",
    backToMarketplace: "← 返回首页",
    detailEyebrow: "校园商品",
    pickup: "交接地点",
    offer: "发起出价",
    seller: "卖家",
    sellerNote: "通常几小时内回复，更倾向在校内熟悉地点完成交接。",
    tags: "标签",
    chat: "联系卖家",
    inbox: "收件箱",
    conversations: "你的聊天消息",
    activeThread: "当前会话",
    message: "消息内容",
    composerPlaceholder: "输入消息，确认价格或交接时间...",
    send: "发送",
    copy: "复制",
    copied: "已复制",
    recall: "撤回",
    recallExpired: "不可撤回",
    recalledMessage: "消息已撤回",
    snippetText1: "今晚 6:30 在图书馆门口见面可以吗？",
    snippetText2: "计算器也可以一起打包给你……",
    strategyEyebrow: "平台策略",
    strategyTitle: "从校园交易工具走向 AI 驱动的平台",
    strategyDesc: "这个方案将学生二手交易、校园商家广告、可信认证和 AI 辅助运营整合到同一个校园产品中。",
    flowTitle1: "认证用户进入平台",
    flowDesc1: "学生、广告主、家教、招聘方和周边商家可以按照不同角色进入系统。",
    flowTitle2: "商品或广告被创建",
    flowDesc2: "二手实物、数字服务、兼职信息和赞助推广内容都进入结构化流程。",
    flowTitle3: "AI 提升内容质量",
    flowDesc3: "AI 可用于文案优化、定价建议、审核提醒、匹配推荐和首轮客服回复。",
    flowTitle4: "线下交接与后续反馈",
    flowDesc4: "用户确认时间地点、收到提醒、完成交接，并留下评分和反馈。",
    layerTitle1: "用户层",
    layerDesc1: "买家、卖家、广告主和管理员共享一套基于校园认证的身份与信用体系。",
    layerTitle2: "入口层",
    layerDesc2: "API 网关、H5 页面、小程序入口和通知渠道把请求安全地接入平台。",
    layerTitle3: "核心业务层",
    layerDesc3: "商品、交易、用户中心、广告系统、评分体系、合规机制和担保支付构成业务核心。",
    layerTitle4: "AI 能力层",
    layerDesc4: "AI 自动补全、价格审核、匹配引擎和 RAG 支持降低摩擦并提升信任与效率。",
    layerTitle5: "基础设施层",
    layerDesc5: "MySQL、Redis、对象存储、消息队列和分析系统保证平台响应、可追踪和可扩展。",
    bizTitle1: "价值主张",
    bizList1: [
      "集中式校园市场减少重复发帖和碎片化搜索。",
      "AI 辅助发布、审核、定价和沟通，降低买卖双方时间成本。",
      "认证信任、评分和结构化交接流程让交易更安全、更清晰。",
    ],
    bizTitle2: "收入来源",
    bizList2: [
      "面向周边商家、招聘方、中介和服务提供者的广告收费。",
      "面向急售卖家的付费曝光和加急推广。",
      "面向校园品牌的首页推荐位和高级活动工具。",
      "面向高信任交易的保证金或担保服务费。",
    ],
    bizTitle3: "独特优势",
    bizList3: [
      "把商品、沟通和决策集中在一个地方，显著节省时间。",
      "通过 AI 文案、成色审核、价格参考和匹配推荐提升准确性。",
      "用 AI 首轮回复降低商家和广告主的响应压力。",
    ],
  },
};

function loadStoredState() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (!raw) {
      return null;
    }
    return JSON.parse(raw);
  } catch {
    return null;
  }
}

const savedState = loadStoredState();
let currentLanguage = localStorage.getItem(LANGUAGE_KEY) || "en";
let activeView = "home";
let activeDetailId = 1;
const initialListingIds = new Set(initialListings.map((item) => item.id));

function normalizeListings(listings) {
  return (listings || []).map((item) => ({
    ...item,
    userCreated: item.userCreated ?? !initialListingIds.has(item.id),
  }));
}

const state = {
  listings: savedState?.listings?.length ? normalizeListings(savedState.listings) : normalizeListings(initialListings),
  wantedPosts: savedState?.wantedPosts?.length ? savedState.wantedPosts : [...initialWantedPosts],
  orders: savedState?.orders || [],
  favorites: new Set(savedState?.favorites || []),
  cart: savedState?.cart || [],
  showFavoritesOnly: false,
};

const dom = {
  listingGrid: document.getElementById("listingGrid"),
  listingTemplate: document.getElementById("listingCardTemplate"),
  searchInput: document.getElementById("searchInput"),
  categoryFilter: document.getElementById("categoryFilter"),
  conditionFilter: document.getElementById("conditionFilter"),
  sortFilter: document.getElementById("sortFilter"),
  priceRange: document.getElementById("priceRange"),
  priceValue: document.getElementById("priceValue"),
  resultsCount: document.getElementById("resultsCount"),
  cartItems: document.getElementById("cartItems"),
  cartCount: document.getElementById("cartCount"),
  cartTotal: document.getElementById("cartTotal"),
  checkoutStatus: document.getElementById("checkoutStatus"),
  checkoutView: document.getElementById("checkoutView"),
  checkoutList: document.getElementById("checkoutList"),
  checkoutItemsCount: document.getElementById("checkoutItemsCount"),
  checkoutTotalValue: document.getElementById("checkoutTotalValue"),
  checkoutForm: document.getElementById("checkoutForm"),
  checkoutConfirmation: document.getElementById("checkoutConfirmation"),
  showFavoritesButton: document.getElementById("showFavorites"),
  resetFiltersButton: document.getElementById("resetFilters"),
  checkoutButton: document.getElementById("checkoutButton"),
  listingForm: document.getElementById("listingForm"),
  imageInput: document.getElementById("imageInput"),
  imagePreviewBox: document.getElementById("imagePreviewBox"),
  imagePreview: document.getElementById("imagePreview"),
  wantedForm: document.getElementById("wantedForm"),
  wantedGrid: document.getElementById("wantedGrid"),
  aiNote: document.getElementById("aiNote"),
  jumpToSell: document.getElementById("jumpToSell"),
  menuToggle: document.getElementById("menuToggle"),
  navbarActions: document.querySelector(".navbar-actions"),
  cartPanel: document.getElementById("cartPanel"),
  exploreNow: document.getElementById("exploreNow"),
  langEn: document.getElementById("langEn"),
  langZh: document.getElementById("langZh"),
  studentVerifiedButton: document.getElementById("studentVerifiedButton"),
  loginLink: document.getElementById("loginLink"),
  myHubToggle: document.getElementById("myHubToggle"),
  myHubPanel: document.getElementById("myHubPanel"),
  myHubMessages: document.getElementById("myHubMessages"),
  myHubCart: document.getElementById("myHubCart"),
  myHubOrders: document.getElementById("myHubOrders"),
  myHubCartLabel: document.getElementById("myHubCartLabel"),
  myHubCartCount: document.getElementById("myHubCartCount"),
  myHubCartTotal: document.getElementById("myHubCartTotal"),
  joinNowLink: document.getElementById("joinNowLink"),
  modeBrowse: document.getElementById("modeBrowse"),
  modeSell: document.getElementById("modeSell"),
  modeWanted: document.getElementById("modeWanted"),
  authView: document.getElementById("authView"),
  detailView: document.getElementById("detailView"),
  chatView: document.getElementById("chatView"),
  ordersView: document.getElementById("ordersView"),
  ordersList: document.getElementById("ordersList"),
  ordersCountValue: document.getElementById("ordersCountValue"),
  ordersLatestValue: document.getElementById("ordersLatestValue"),
  loginTab: document.getElementById("loginTab"),
  registerTab: document.getElementById("registerTab"),
  loginForm: document.getElementById("loginForm"),
  registerForm: document.getElementById("registerForm"),
  detailImage: document.getElementById("detailImage"),
  detailTitle: document.getElementById("detailTitle"),
  detailDescription: document.getElementById("detailDescription"),
  detailPrice: document.getElementById("detailPrice"),
  detailPriceMirror: document.getElementById("detailPriceMirror"),
  detailCondition: document.getElementById("detailCondition"),
  detailLocation: document.getElementById("detailLocation"),
  detailRating: document.getElementById("detailRating"),
  detailSeller: document.getElementById("detailSeller"),
  detailTags: document.getElementById("detailTags"),
  detailCartButton: document.getElementById("detailCartButton"),
  chatSellerLink: document.getElementById("chatSellerLink"),
  conversationList: document.getElementById("conversationList"),
  threadTitle: document.getElementById("threadTitle"),
  messageThread: document.getElementById("messageThread"),
  chatComposer: document.getElementById("chatComposer"),
  composerInput: document.getElementById("composerInput"),
};

const views = {
  auth: dom.authView,
  detail: dom.detailView,
  chat: dom.chatView,
  checkout: dom.checkoutView,
  orders: dom.ordersView,
};

let chatConversations = [];
let activeConversationId = 1;
let pendingOrderMessage = "";
let pendingOrderItemId = null;
let uploadedListingImage = "";
const MESSAGE_RECALL_WINDOW_MS = 2 * 60 * 1000;

function t(key) {
  return uiText[currentLanguage][key] || uiText.en[key] || key;
}

function formatCurrency(value) {
  return currentLanguage === "zh" ? `人民币 ${value}` : `RMB ${value}`;
}

function getListingText(item, key) {
  if (currentLanguage === "zh" && item[`${key}Zh`]) {
    return item[`${key}Zh`];
  }
  return item[key];
}

function createListingVisual(item) {
  const paletteMap = {
    Textbooks: ["#5c3b93", "#7b1e3a"],
    Electronics: ["#2f5d8a", "#5c3b93"],
    "Lifestyle Essentials": ["#8a5a2f", "#5c3b93"],
    Fashion: ["#7b1e3a", "#452a73"],
  };
  const [from, to] = paletteMap[item.category] || ["#5c3b93", "#7b1e3a"];
  const title = getListingText(item, "title")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
  const category = getListingText(item, "category")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
  const svg = `
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
      <defs>
        <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0%" stop-color="${from}"/>
          <stop offset="100%" stop-color="${to}"/>
        </linearGradient>
      </defs>
      <rect width="800" height="600" fill="url(#g)"/>
      <circle cx="680" cy="120" r="110" fill="rgba(255,255,255,0.12)"/>
      <circle cx="140" cy="500" r="150" fill="rgba(255,255,255,0.08)"/>
      <rect x="54" y="56" rx="22" ry="22" width="220" height="56" fill="rgba(255,255,255,0.16)"/>
      <text x="84" y="92" font-family="Arial, sans-serif" font-size="28" fill="white">${category}</text>
      <text x="58" y="250" font-family="Arial, sans-serif" font-size="50" font-weight="700" fill="white">${title}</text>
      <text x="58" y="314" font-family="Arial, sans-serif" font-size="24" fill="rgba(255,255,255,0.82)">CampuX Demo</text>
    </svg>
  `;
  return `url("data:image/svg+xml;charset=UTF-8,${encodeURIComponent(svg)}")`;
}

function getListingImage(item) {
  if (item.image) {
    return item.image;
  }
  return createListingVisual(item).slice(5, -2);
}

function getListingById(id) {
  return state.listings.find((item) => item.id === id) || state.listings[0];
}

function canRecallMessage(message) {
  return message.self && !message.recalled && Date.now() - (message.sentAt || 0) <= MESSAGE_RECALL_WINDOW_MS;
}

async function copyMessageText(text) {
  if (navigator.clipboard?.writeText) {
    await navigator.clipboard.writeText(text);
    return;
  }

  const helper = document.createElement("textarea");
  helper.value = text;
  document.body.appendChild(helper);
  helper.select();
  document.execCommand("copy");
  document.body.removeChild(helper);
}

function persistState() {
  localStorage.setItem(
    STORAGE_KEY,
    JSON.stringify({
      listings: state.listings,
      wantedPosts: state.wantedPosts,
      orders: state.orders,
      favorites: [...state.favorites],
      cart: state.cart,
    })
  );
}

function syncLanguageButtons() {
  dom.langEn.classList.toggle("active", currentLanguage === "en");
  dom.langZh.classList.toggle("active", currentLanguage === "zh");
}

function applyStaticText() {
  document.documentElement.lang = currentLanguage === "zh" ? "zh-CN" : "en";
  const categoryOptions = document.querySelectorAll("#formCategory option");
  const wantedCategoryOptions = document.querySelectorAll("#wantedCategory option");
  const formConditionOptions = document.querySelectorAll("#formCondition option");
  const filterConditionOptions = document.querySelectorAll("#conditionFilter option");

  dom.studentVerifiedButton.textContent = t("studentVerified");
  dom.menuToggle.textContent = dom.navbarActions.classList.contains("open") ? t("closeMenu") : t("menu");
  dom.loginLink.textContent = t("login");
  dom.myHubToggle.textContent = t("myHub");
  dom.myHubMessages.textContent = t("messages");
  dom.myHubCart.textContent = t("viewCart");
  dom.myHubOrders.textContent = t("orders");
  dom.myHubCartLabel.textContent = t("cartShort");
  dom.jumpToSell.textContent = t("jumpToSell");
  document.getElementById("heroTag").textContent = t("heroTag");
  document.getElementById("heroTitle").textContent =
    currentLanguage === "zh" ? "买得更聪明，卖得更轻松。" : "Buy smarter. Sell faster.";
  document.getElementById("heroDescription").textContent =
    currentLanguage === "zh"
      ? "面向校园生活场景的可信二手交易平台。"
      : "The trusted second-hand marketplace built for campus life.";
  dom.exploreNow.textContent = t("exploreNow");
  dom.joinNowLink.textContent = currentLanguage === "zh" ? "加入市场" : "Join Market";
  dom.modeBrowse.textContent = t("modeBrowse");
  dom.modeSell.textContent = t("modeSell");
  dom.modeWanted.textContent = t("modeWanted");
  document.getElementById("heroStat1").textContent = currentLanguage === "zh" ? "活跃商品" : "Active listings";
  document.getElementById("heroStat2").textContent = currentLanguage === "zh" ? "学生认证" : "Verified students";
  document.getElementById("heroStat3").textContent = currentLanguage === "zh" ? "平均收到报价" : "Avg. offer time";
  document.getElementById("galleryEyebrow").textContent = t("galleryEyebrow");
  document.getElementById("galleryTitle").textContent = t("galleryTitle");
  document.getElementById("galleryDesc").textContent = t("galleryDesc");
  document.getElementById("galleryBadge").textContent = t("galleryBadge");
  document.getElementById("marketplaceEyebrow").textContent = t("marketplaceEyebrow");
  document.getElementById("marketplaceTitle").textContent = t("marketplaceTitle");
  document.getElementById("marketplaceDesc").textContent = t("marketplaceDesc");
  dom.categoryFilter.options[0].textContent = t("allCategories");
  filterConditionOptions[0].textContent = t("allConditions");
  filterConditionOptions[1].textContent = t("likeNew");
  filterConditionOptions[2].textContent = t("good");
  filterConditionOptions[3].textContent = t("fair");
  filterConditionOptions[4].textContent = t("worn");
  dom.sortFilter.options[0].textContent = t("recommended");
  dom.sortFilter.options[1].textContent = t("lowToHigh");
  dom.sortFilter.options[2].textContent = t("highToLow");
  dom.sortFilter.options[3].textContent = t("sellerRating");
  document.getElementById("maxPriceLabel").textContent = currentLanguage === "zh" ? "最高:" : "Max:";
  dom.showFavoritesButton.textContent = state.showFavoritesOnly ? t("showingFavorites") : t("favorites");
  dom.resetFiltersButton.textContent = t("reset");
  document.getElementById("cartTitle").textContent = currentLanguage === "zh" ? "你的购物车" : "Your Cart";
  document.getElementById("totalLabel").textContent = t("total");
  dom.checkoutButton.textContent = currentLanguage === "zh" ? "结算" : "Checkout";
  dom.checkoutStatus.textContent = currentLanguage === "zh" ? "预留商品并安排校内交接。" : "Reserve for campus handoff.";
  document.getElementById("messagesTitle").textContent = currentLanguage === "zh" ? "最近消息" : "Recent Messages";
  document.getElementById("snippetText1").textContent = t("snippetText1");
  document.getElementById("snippetText2").textContent = t("snippetText2");
  document.getElementById("sellEyebrow").textContent = t("sellEyebrow");
  document.getElementById("sellTitle").textContent = currentLanguage === "zh" ? "发布商品" : "Post a Listing";
  document.getElementById("sellDesc").textContent = currentLanguage === "zh" ? "结合 AI 辅助的快速发布表单。" : "Smart posting with AI formatting assistance.";
  document.getElementById("itemTitleLabel").textContent = t("itemTitle");
  document.getElementById("imageUploadLabel").textContent = t("imageUpload");
  document.getElementById("imageUploadHint").textContent = t("imageUploadHint");
  document.getElementById("categoryLabelMain").textContent = t("category");
  document.getElementById("priceLabelMain").textContent = t("price");
  document.getElementById("conditionLabelMain").textContent = t("condition");
  document.getElementById("sellerNameLabel").textContent = t("sellerName");
  document.getElementById("pickupPointLabel").textContent = t("pickupPoint");
  document.getElementById("descriptionLabel").textContent = t("description");
  categoryOptions[0].textContent = t("chooseCategory");
  categoryOptions[1].textContent = t("textbooks");
  categoryOptions[2].textContent = t("electronics");
  categoryOptions[3].textContent = t("dormEssentials");
  categoryOptions[4].textContent = t("fashion");
  wantedCategoryOptions[0].textContent = t("chooseCategory");
  wantedCategoryOptions[1].textContent = t("textbooks");
  wantedCategoryOptions[2].textContent = t("electronics");
  wantedCategoryOptions[3].textContent = t("dormEssentials");
  wantedCategoryOptions[4].textContent = t("fashion");
  formConditionOptions[0].textContent = t("chooseCondition");
  formConditionOptions[1].textContent = t("likeNew");
  formConditionOptions[2].textContent = t("good");
  formConditionOptions[3].textContent = t("fair");
  formConditionOptions[4].textContent = t("worn");
  document.getElementById("generateAiCopy").textContent = t("generateAi");
  document.getElementById("publishButton").textContent = t("publish");
  document.getElementById("wantedEyebrow").textContent = t("wantedEyebrow");
  document.getElementById("wantedTitle").textContent = t("wantedTitle");
  document.getElementById("wantedDesc").textContent = t("wantedDesc");
  document.getElementById("wantedItemLabel").textContent = t("wantedItem");
  document.getElementById("wantedBudgetLabel").textContent = t("wantedBudget");
  document.getElementById("wantedCategoryLabel").textContent = t("category");
  document.getElementById("wantedBuyerLabel").textContent = t("wantedBuyer");
  document.getElementById("wantedLocationLabel").textContent = t("wantedLocation");
  document.getElementById("wantedDescriptionLabel").textContent = t("wantedDetails");
  document.getElementById("wantedPublishButton").textContent = t("wantedPublish");
  dom.searchInput.placeholder = t("searchPlaceholder");
  document.getElementById("titleInput").placeholder = t("titlePlaceholder");
  document.getElementById("sellerInput").placeholder = t("sellerPlaceholder");
  document.getElementById("locationInput").placeholder = t("locationPlaceholder");
  document.getElementById("descriptionInput").placeholder = t("descriptionPlaceholder");
  document.getElementById("wantedTitleInput").placeholder = t("wantedPlaceholder");
  document.getElementById("wantedBuyerInput").placeholder = t("sellerPlaceholder");
  document.getElementById("wantedLocationInput").placeholder = t("locationPlaceholder");
  document.getElementById("wantedDescriptionInput").placeholder = t("wantedDescriptionPlaceholder");
  dom.aiNote.textContent = t("aiInitial");
  document.getElementById("wantedNote").textContent = t("wantedInitial");

  applyAuthCopy();
  applyChatCopy();
  syncLanguageButtons();
}

function closeNavbarMenu() {
  dom.navbarActions.classList.remove("open");
  dom.menuToggle.setAttribute("aria-expanded", "false");
  dom.menuToggle.textContent = t("menu");
  closeMyHub();
}

function toggleNavbarMenu() {
  const willOpen = !dom.navbarActions.classList.contains("open");
  dom.navbarActions.classList.toggle("open", willOpen);
  dom.menuToggle.setAttribute("aria-expanded", willOpen ? "true" : "false");
  dom.menuToggle.textContent = willOpen ? t("closeMenu") : t("menu");
  if (!willOpen) closeMyHub();
}

function closeMyHub() {
  dom.myHubPanel.classList.add("hidden-view");
  dom.myHubToggle.setAttribute("aria-expanded", "false");
}

function toggleMyHub() {
  const willOpen = dom.myHubPanel.classList.contains("hidden-view");
  dom.myHubPanel.classList.toggle("hidden-view", !willOpen);
  dom.myHubToggle.setAttribute("aria-expanded", willOpen ? "true" : "false");
}

function populateCategories() {
  const currentValue = dom.categoryFilter.value;
  dom.categoryFilter.innerHTML = `<option value="All">${t("allCategories")}</option>`;
  const categories = [...new Set(state.listings.map((item) => item.category))];
  categories.forEach((category) => {
    const option = document.createElement("option");
    option.value = category;
    const tempItem = state.listings.find((item) => item.category === category);
    option.textContent = getListingText(tempItem, "category");
    dom.categoryFilter.appendChild(option);
  });
  dom.categoryFilter.value = [...dom.categoryFilter.options].some((option) => option.value === currentValue)
    ? currentValue
    : "All";
}

function getFilteredListings() {
  const keyword = dom.searchInput.value.trim().toLowerCase();
  const selectedCategory = dom.categoryFilter.value;
  const selectedCondition = dom.conditionFilter.value;
  const maxPrice = Number(dom.priceRange.value);

  let filtered = state.listings.filter((item) => {
    const searchableStrings = [
      item.title,
      item.titleZh,
      item.seller,
      item.description,
      item.descriptionZh,
      ...(item.tags || []),
      ...(item.tagsZh || []),
    ]
      .filter(Boolean)
      .map((text) => text.toLowerCase());

    const matchesKeyword = keyword === "" || searchableStrings.some((text) => text.includes(keyword));
    const matchesCategory = selectedCategory === "All" || item.category === selectedCategory;
    const matchesCondition = selectedCondition === "All" || item.condition === selectedCondition;
    const matchesPrice = item.price <= maxPrice;
    const matchesFavorites = !state.showFavoritesOnly || state.favorites.has(item.id);
    return matchesKeyword && matchesCategory && matchesCondition && matchesPrice && matchesFavorites;
  });

  if (dom.sortFilter.value === "price-asc") filtered = filtered.sort((a, b) => a.price - b.price);
  if (dom.sortFilter.value === "price-desc") filtered = filtered.sort((a, b) => b.price - a.price);
  if (dom.sortFilter.value === "rating-desc") filtered = filtered.sort((a, b) => b.rating - a.rating);
  return filtered;
}

function renderListings() {
  const filtered = getFilteredListings();
  dom.listingGrid.innerHTML = "";
  dom.resultsCount.textContent =
    currentLanguage === "zh"
      ? `${filtered.length}${t("listings")}`
      : `${filtered.length} ${filtered.length === 1 ? t("listing") : t("listings")}`;

  if (filtered.length === 0) {
    const emptyState = document.createElement("div");
    emptyState.className = "empty-state";
    emptyState.textContent = t("emptyListings");
    dom.listingGrid.appendChild(emptyState);
    return;
  }

  filtered.forEach((item) => {
    const node = dom.listingTemplate.content.cloneNode(true);
    node.querySelector(".listing-badge").textContent = getListingText(item, "badge");
    node.querySelector(".listing-visual").style.backgroundImage = `url("${getListingImage(item)}")`;
    node.querySelector(".listing-category").textContent = getListingText(item, "category");
    node.querySelector(".listing-condition").textContent = getListingText(item, "condition");
    node.querySelector(".listing-title").textContent = getListingText(item, "title");
    node.querySelector(".listing-description").textContent = getListingText(item, "description");
    node.querySelector(".listing-seller").textContent = item.seller;
    node.querySelector(".listing-rating").textContent = `${item.rating} ${t("ratingSuffix")}`;
    node.querySelector(".listing-price").textContent = formatCurrency(item.price);
    node.querySelector(".listing-location").textContent = getListingText(item, "location");

    const favoriteButton = node.querySelector(".favorite-button");
    if (state.favorites.has(item.id)) {
      favoriteButton.classList.add("active");
      favoriteButton.innerHTML = "&#9829;";
    }
    favoriteButton.addEventListener("click", () => toggleFavorite(item.id));

    const tagsContainer = node.querySelector(".listing-tags");
    const tags = currentLanguage === "zh" && item.tagsZh ? item.tagsZh : item.tags;
    tags.forEach((tag) => {
      const pill = document.createElement("span");
      pill.textContent = tag;
      tagsContainer.appendChild(pill);
    });

    const addToCartButton = node.querySelector(".add-cart-button");
    addToCartButton.textContent = t("addToCart");
    addToCartButton.addEventListener("click", () => addToCart(item.id));
    const detailsLink = node.querySelector(".details-link");
    detailsLink.textContent = t("details");
    detailsLink.addEventListener("click", () => openDetailView(item.id));
    if (item.userCreated) {
      const deleteButton = document.createElement("button");
      deleteButton.type = "button";
      deleteButton.className = "btn-ghost small";
      deleteButton.textContent = t("deleteListing");
      deleteButton.addEventListener("click", () => deleteListing(item.id));
      node.querySelector(".listing-actions").appendChild(deleteButton);
    }

    dom.listingGrid.appendChild(node);
  });
}

function toggleFavorite(id) {
  if (state.favorites.has(id)) state.favorites.delete(id);
  else state.favorites.add(id);
  persistState();
  renderListings();
}

function addToCart(id) {
  const item = getListingById(id);
  const existingItem = state.cart.find((entry) => entry.id === id);
  if (existingItem) existingItem.quantity += 1;
  else state.cart.push({ ...item, quantity: 1 });
  persistState();
  renderCart();
}

function removeFromCart(id) {
  state.cart = state.cart.filter((item) => item.id !== id);
  persistState();
  renderCart();
}

function deleteListing(id) {
  state.listings = state.listings.filter((item) => item.id !== id);
  state.favorites.delete(id);
  state.cart = state.cart.filter((item) => item.id !== id);
  if (activeDetailId === id) {
    hideViews();
  }
  persistState();
  populateCategories();
  renderListings();
  renderCart();
}

function renderCart() {
  dom.cartItems.innerHTML = "";
  if (state.cart.length === 0) {
    const emptyState = document.createElement("div");
    emptyState.className = "empty-state";
    emptyState.textContent = t("emptyCart");
    dom.cartItems.appendChild(emptyState);
  } else {
    state.cart.forEach((item) => {
      const card = document.createElement("article");
      card.className = "cart-item";
      card.innerHTML = `
        <div class="cart-item-header">
          <strong>${getListingText(item, "title")}</strong>
          <button class="text-button" type="button">${t("remove")}</button>
        </div>
        <p>${getListingText(item, "location")}</p>
        <div class="cart-item-footer">
          <span>${t("qty")} ${item.quantity}</span>
          <strong>${formatCurrency(item.price * item.quantity)}</strong>
        </div>
      `;
      card.querySelector("button").addEventListener("click", () => removeFromCart(item.id));
      dom.cartItems.appendChild(card);
    });
  }

  const total = state.cart.reduce((sum, item) => sum + item.price * item.quantity, 0);
  const quantity = state.cart.reduce((sum, item) => sum + item.quantity, 0);
  dom.cartCount.textContent = `${quantity}`;
  dom.cartTotal.textContent = formatCurrency(total);
  dom.myHubCartCount.textContent =
    currentLanguage === "zh" ? `${quantity}${t("cartItemsCount")}` : `${quantity} ${t("cartItemsCount")}`;
  dom.myHubCartTotal.textContent = formatCurrency(total);
}

function renderCheckoutView() {
  dom.checkoutList.innerHTML = "";
  state.cart.forEach((item) => {
    const row = document.createElement("article");
    row.className = "checkout-item";
    row.innerHTML = `
      <div>
        <strong>${getListingText(item, "title")}</strong>
        <p>${getListingText(item, "location")}</p>
      </div>
      <div class="checkout-item-meta">
        <span>${t("qty")} ${item.quantity}</span>
        <strong>${formatCurrency(item.price * item.quantity)}</strong>
      </div>
    `;
    dom.checkoutList.appendChild(row);
  });
  const total = state.cart.reduce((sum, item) => sum + item.price * item.quantity, 0);
  const quantity = state.cart.reduce((sum, item) => sum + item.quantity, 0);
  dom.checkoutItemsCount.textContent = `${quantity}`;
  dom.checkoutTotalValue.textContent = formatCurrency(total);
}

function renderOrdersView() {
  dom.ordersList.innerHTML = "";
  if (state.orders.length === 0) {
    const emptyState = document.createElement("div");
    emptyState.className = "empty-state";
    emptyState.textContent = t("ordersEmpty");
    dom.ordersList.appendChild(emptyState);
    dom.ordersCountValue.textContent = "0";
    dom.ordersLatestValue.textContent = "-";
    return;
  }

  state.orders.forEach((order) => {
    const row = document.createElement("article");
    row.className = "checkout-item";
    row.innerHTML = `
      <div>
        <strong>${order.id}</strong>
        <p>${order.itemsSummary}</p>
        <p>${order.pickup} · ${order.time}</p>
      </div>
      <div class="checkout-item-meta">
        <span>${t("ordersStatus")}</span>
        <strong>${order.total}</strong>
      </div>
    `;
    dom.ordersList.appendChild(row);
  });

  dom.ordersCountValue.textContent = `${state.orders.length}`;
  dom.ordersLatestValue.textContent = state.orders[0].id;
}

function openCheckoutView() {
  if (state.cart.length === 0) {
    dom.checkoutStatus.textContent = t("addItemsFirst");
    return;
  }
  dom.checkoutForm.classList.remove("hidden-view");
  dom.checkoutConfirmation.classList.add("hidden-view");
  document.getElementById("checkoutPageStatus").textContent = t("checkoutPageHint");
  renderCheckoutView();
  showView("checkout");
}

function renderWantedPosts() {
  dom.wantedGrid.innerHTML = "";
  state.wantedPosts.forEach((item) => {
    const card = document.createElement("article");
    card.className = "wanted-card";
    const tags = currentLanguage === "zh" && item.tagsZh ? item.tagsZh : item.tags;
    const category = getListingText(item, "category");
    const title = getListingText(item, "title");
    const description = getListingText(item, "description");
    const location = getListingText(item, "location");
    const badge = getListingText(item, "badge");
    card.innerHTML = `
      <div class="wanted-card-top">
        <span class="wanted-badge">${badge}</span>
        <strong>${t("budgetLabel")}: ${formatCurrency(item.budget)}</strong>
      </div>
      <div class="wanted-meta">${category}</div>
      <h3>${title}</h3>
      <p>${description}</p>
      <div class="wanted-tags"></div>
      <div class="wanted-footer">
        <div>
          <strong>${item.buyer}</strong>
          <span>${location}</span>
        </div>
      </div>
    `;
    const tagWrap = card.querySelector(".wanted-tags");
    tags.forEach((tag) => {
      const pill = document.createElement("span");
      pill.textContent = tag;
      tagWrap.appendChild(pill);
    });
    dom.wantedGrid.appendChild(card);
  });
}

function resetFilters() {
  dom.searchInput.value = "";
  dom.categoryFilter.value = "All";
  dom.conditionFilter.value = "All";
  dom.sortFilter.value = "default";
  dom.priceRange.value = "3000";
  dom.priceValue.textContent = "3000";
  state.showFavoritesOnly = false;
  dom.showFavoritesButton.textContent = t("favorites");
  renderListings();
}

function createAiDescription() {
  const title = document.getElementById("titleInput").value.trim();
  const category = document.getElementById("formCategory").value;
  const price = document.getElementById("priceInput").value.trim();
  const seller = document.getElementById("sellerInput").value.trim() || (currentLanguage === "zh" ? "校园同学" : "a fellow student");
  const location = document.getElementById("locationInput").value.trim() || (currentLanguage === "zh" ? "校内交接点" : "a campus pick-up point");
  const descriptionField = document.getElementById("descriptionInput");

  if (!title || !category) {
    dom.aiNote.textContent = t("aiNeedInput");
    return;
  }

  descriptionField.value =
    currentLanguage === "zh"
      ? `${title}，分类为${category}，由${seller}发布。商品状态良好，适合校园日常使用，可在${location}当面交接。目前定价为${price || t("defaultAiPrice")}元，支持合理议价，适合快速完成校园二手交易。`
      : `${title} in ${category.toLowerCase()} category, offered by ${seller}. Kept in reliable condition and suitable for student use. Pick-up is available at ${location}. Current asking price is ${price || t("defaultAiPrice")} RMB, and the seller is open to reasonable campus offers for a quick and smooth transaction.`;

  dom.aiNote.textContent = t("aiGenerated");
}

function clearListingImagePreview() {
  uploadedListingImage = "";
  dom.imageInput.value = "";
  dom.imagePreview.removeAttribute("src");
  dom.imagePreviewBox.classList.add("hidden-view");
}

function handleListingImageChange(event) {
  const [file] = event.target.files || [];
  if (!file) {
    clearListingImagePreview();
    return;
  }

  const reader = new FileReader();
  reader.onload = () => {
    uploadedListingImage = reader.result;
    dom.imagePreview.src = uploadedListingImage;
    dom.imagePreviewBox.classList.remove("hidden-view");
  };
  reader.readAsDataURL(file);
}

function handleFormSubmit(event) {
  event.preventDefault();
  const categoryValue = document.getElementById("formCategory").value;
  const conditionValue = document.getElementById("formCondition").value;
  const titleValue = document.getElementById("titleInput").value.trim();
  const locationValue = document.getElementById("locationInput").value.trim();
  const descriptionValue = document.getElementById("descriptionInput").value.trim();

  const newListing = {
    id: Date.now(),
    userCreated: true,
    title: titleValue,
    titleZh: titleValue,
    category: categoryValue,
    categoryZh: mapCategoryToZh(categoryValue),
    price: Number(document.getElementById("priceInput").value),
    condition: conditionValue,
    conditionZh: mapConditionToZh(conditionValue),
    seller: document.getElementById("sellerInput").value.trim(),
    rating: 5.0,
    location: locationValue,
    locationZh: locationValue,
    badge: t("newListing"),
    badgeZh: t("newListing"),
    description: descriptionValue,
    descriptionZh: descriptionValue,
    tags: [t("studentPost"), t("fresh"), t("campusDeal")],
    tagsZh: [t("studentPost"), t("fresh"), t("campusDeal")],
    image: uploadedListingImage || createListingVisual({ category: categoryValue, title: titleValue, titleZh: titleValue }).slice(5, -2),
  };

  state.listings.unshift(newListing);
  persistState();
  populateCategories();
  dom.listingForm.reset();
  clearListingImagePreview();
  dom.aiNote.textContent = t("published");
  renderListings();
  setPrimarySection("browse");
}

function handleWantedSubmit(event) {
  event.preventDefault();
  const categoryValue = document.getElementById("wantedCategory").value;
  const titleValue = document.getElementById("wantedTitleInput").value.trim();
  const locationValue = document.getElementById("wantedLocationInput").value.trim();
  const descriptionValue = document.getElementById("wantedDescriptionInput").value.trim();

  const wantedPost = {
    id: Date.now(),
    title: titleValue,
    titleZh: titleValue,
    category: categoryValue,
    categoryZh: mapCategoryToZh(categoryValue),
    budget: Number(document.getElementById("wantedBudgetInput").value),
    buyer: document.getElementById("wantedBuyerInput").value.trim(),
    buyerZh: document.getElementById("wantedBuyerInput").value.trim(),
    location: locationValue,
    locationZh: locationValue,
    badge: t("wantedTag"),
    badgeZh: t("wantedTag"),
    description: descriptionValue,
    descriptionZh: descriptionValue,
    tags: [t("wantedTag"), t("fresh"), t("campusDeal")],
    tagsZh: [t("wantedTag"), t("fresh"), t("campusDeal")],
  };

  state.wantedPosts.unshift(wantedPost);
  persistState();
  dom.wantedForm.reset();
  document.getElementById("wantedNote").textContent = t("wantedPublished");
  renderWantedPosts();
  setPrimarySection("wanted");
}

function mapCategoryToZh(category) {
  const map = {
    Textbooks: "教材资料",
    Electronics: "数码电子",
    "Lifestyle Essentials": "生活用品",
    Fashion: "服饰鞋包",
  };
  return map[category] || category;
}

function mapConditionToZh(condition) {
  const map = {
    "Brand New": "全新",
    "Light Signs of Use": "轻微使用痕迹",
    "Visible Signs of Use": "明显使用痕迹",
    Stained: "污损",
  };
  return map[condition] || condition;
}

function setPrimarySection(sectionName, options = {}) {
  const { smooth = true } = options;
  const sections = {
    browse: document.getElementById("marketplace"),
    sell: document.getElementById("sellSection"),
    wanted: document.getElementById("wantedSection"),
  };

  Object.entries(sections).forEach(([key, element]) => {
    element.classList.toggle("hidden-view", key !== sectionName);
  });

  dom.modeBrowse.classList.toggle("active", sectionName === "browse");
  dom.modeSell.classList.toggle("active", sectionName === "sell");
  dom.modeWanted.classList.toggle("active", sectionName === "wanted");

  sections[sectionName].scrollIntoView({ behavior: smooth ? "smooth" : "auto", block: "start" });
}

function showView(name) {
  activeView = name;
  Object.entries(views).forEach(([key, element]) => {
    element.classList.toggle("hidden-view", key !== name);
  });
}

function hideViews() {
  activeView = "home";
  Object.values(views).forEach((element) => element.classList.add("hidden-view"));
}

function applyAuthCopy() {
  document.querySelector('[data-close-view="auth"]').textContent = currentLanguage === "zh" ? "关闭" : "Close";
  document.querySelector('[data-close-view="detail"]').textContent = t("backToMarketplace");
  document.querySelector('[data-close-view="chat"]').textContent = currentLanguage === "zh" ? "返回" : "Back";
  document.getElementById("authEyebrow").textContent = t("authEyebrow");
  document.getElementById("authTitle").textContent = t("authTitle");
  document.getElementById("authLead").textContent = t("authLead");
  dom.loginTab.textContent = t("loginTab");
  dom.registerTab.textContent = t("registerTab");
  document.getElementById("emailLabel").textContent = t("email");
  document.getElementById("passwordLabel").textContent = t("password");
  document.getElementById("studentIdLabel").textContent = t("studentId");
  document.getElementById("loginSubmit").textContent = t("loginSubmit");
  document.getElementById("nameLabel").textContent = t("fullName");
  document.getElementById("collegeLabel").textContent = t("college");
  document.getElementById("registerEmailLabel").textContent = t("campusEmail");
  document.getElementById("registerPasswordLabel").textContent = t("createPassword");
  document.getElementById("pickupPrefLabel").textContent = t("pickupPreference");
  document.getElementById("registerSubmit").textContent = t("registerSubmit");
  document.getElementById("authNote").textContent = t("authNote");
  document.querySelector('[data-close-view="checkout"]').textContent = currentLanguage === "zh" ? "返回" : "Back";
  document.getElementById("checkoutEyebrow").textContent = t("checkoutEyebrow");
  document.getElementById("checkoutTitle").textContent = t("checkoutTitle");
  document.getElementById("checkoutLead").textContent = t("checkoutLead");
  document.getElementById("checkoutNameLabel").textContent = t("checkoutName");
  document.getElementById("checkoutPhoneLabel").textContent = t("checkoutPhone");
  document.getElementById("checkoutPickupLabel").textContent = t("checkoutPickupPoint");
  document.getElementById("checkoutTimeLabel").textContent = t("checkoutTime");
  document.getElementById("checkoutMessageLabel").textContent = t("checkoutMessage");
  document.getElementById("checkoutConfirmButton").textContent = t("checkoutConfirm");
  document.getElementById("checkoutSummaryTitle").textContent = t("checkoutSummary");
  document.getElementById("checkoutItemsLabel").textContent = t("checkoutItems");
  document.getElementById("checkoutTotalLabel").textContent = t("total");
  document.getElementById("checkoutPageStatus").textContent = t("checkoutPageHint");
  document.getElementById("checkoutSuccessEyebrow").textContent = t("checkoutSuccessEyebrow");
  document.getElementById("checkoutSuccessTitle").textContent = t("checkoutSuccessTitle");
  document.getElementById("checkoutOrderIdLabel").textContent = t("checkoutOrderId");
  document.getElementById("checkoutPickupConfirmLabel").textContent = t("checkoutPickupPoint");
  document.getElementById("checkoutTimeConfirmLabel").textContent = t("checkoutTime");
  document.getElementById("checkoutContactConfirmLabel").textContent = t("checkoutPhone");
  document.getElementById("ordersEyebrow").textContent = t("ordersEyebrow");
  document.getElementById("ordersTitle").textContent = t("ordersTitle");
  document.getElementById("ordersLead").textContent = t("ordersLead");
  document.getElementById("ordersSummaryTitle").textContent = t("ordersSummary");
  document.getElementById("ordersCountLabel").textContent = t("ordersCount");
  document.getElementById("ordersLatestLabel").textContent = t("ordersLatest");
}

function setAuthTab(isLogin) {
  dom.loginTab.classList.toggle("active", isLogin);
  dom.registerTab.classList.toggle("active", !isLogin);
  dom.loginForm.classList.toggle("active", isLogin);
  dom.registerForm.classList.toggle("active", !isLogin);
  dom.loginForm.style.display = isLogin ? "grid" : "none";
  dom.registerForm.style.display = isLogin ? "none" : "grid";
}

function openDetailView(id) {
  activeDetailId = id;
  renderDetailView();
  showView("detail");
}

function renderDetailView() {
  const item = getListingById(activeDetailId);
  document.getElementById("detailEyebrow").textContent = t("detailEyebrow");
  dom.detailImage.src = getListingImage(item);
  dom.detailTitle.textContent = getListingText(item, "title");
  dom.detailDescription.textContent = getListingText(item, "description");
  document.getElementById("priceLabel").textContent = t("price");
  document.getElementById("detailConditionLabel").textContent = t("condition");
  document.getElementById("locationLabel").textContent = t("pickup");
  document.getElementById("ratingLabel").textContent = t("sellerRating");
  dom.detailPrice.textContent = formatCurrency(item.price);
  if (dom.detailPriceMirror) dom.detailPriceMirror.textContent = formatCurrency(item.price);
  dom.detailCondition.textContent = getListingText(item, "condition");
  dom.detailLocation.textContent = getListingText(item, "location");
  dom.detailRating.textContent = `${item.rating} ${t("ratingSuffix")}`;
  dom.detailSeller.textContent = item.seller;
  document.getElementById("sellerEyebrow").textContent = t("seller");
  document.getElementById("sellerNote").textContent = t("sellerNote");
  document.getElementById("tagsEyebrow").textContent = t("tags");
  dom.detailCartButton.textContent = t("addToCart");
  dom.chatSellerLink.textContent = t("chat");
  document.getElementById("makeOfferLink").textContent = t("offer");
  dom.detailTags.innerHTML = "";
  const tags = currentLanguage === "zh" && item.tagsZh ? item.tagsZh : item.tags;
  tags.forEach((tag) => {
    const pill = document.createElement("span");
    pill.textContent = tag;
    dom.detailTags.appendChild(pill);
  });
}

function buildChatConversations() {
  const item = pendingOrderItemId ? getListingById(pendingOrderItemId) : getListingById(activeDetailId);
  const now = Date.now();
  const firstConversation = {
    id: 1,
    seller: item.seller,
    itemTitle: getListingText(item, "title"),
    preview: currentLanguage === "zh" ? "今晚图书馆门口可以见面吗？" : "Could we meet outside the library tonight?",
    messages: [
      { self: false, text: currentLanguage === "zh" ? "你好，这个商品还在吗？" : "Hi, is this item still available?", sentAt: now - 18 * 60 * 1000 },
      { self: true, text: currentLanguage === "zh" ? "还在的，你想什么时候取？" : "Yes, it is. When would you like to pick it up?", sentAt: now - 16 * 60 * 1000 },
      { self: false, text: currentLanguage === "zh" ? "今晚图书馆门口可以见面吗？" : "Could we meet outside the library tonight?", sentAt: now - 14 * 60 * 1000 },
    ],
  };
  if (pendingOrderMessage) {
    firstConversation.messages.push({ self: true, text: pendingOrderMessage, sentAt: now, recalled: false });
    firstConversation.preview = pendingOrderMessage;
  }
  chatConversations = [
    firstConversation,
    {
      id: 2,
      seller: "Mia Chen",
      itemTitle: currentLanguage === "zh" ? "宿舍台灯与收纳架" : "Dorm Desk Lamp and Storage Rack",
      preview: currentLanguage === "zh" ? "我可以一起打包带走。" : "I can take the bundle together.",
      messages: [
        { self: false, text: currentLanguage === "zh" ? "如果你要两个我可以便宜一点。" : "I can discount it if you take both.", sentAt: now - 30 * 60 * 1000 },
        { self: true, text: currentLanguage === "zh" ? "可以，今晚宿舍楼下见。" : "Sounds good, let's meet near the dorm tonight.", sentAt: now - 28 * 60 * 1000 },
      ],
    },
  ];
  activeConversationId = 1;
}

function applyChatCopy() {
  document.getElementById("chatEyebrow").textContent = t("inbox");
  document.getElementById("chatTitle").textContent = currentLanguage === "zh" ? "消息列表" : "Inbox";
  document.getElementById("threadEyebrow").textContent = t("activeThread");
  document.getElementById("composerLabel").textContent = t("message");
  dom.composerInput.placeholder = t("composerPlaceholder");
  document.getElementById("sendButton").textContent = t("send");
}

function renderChatSidebar() {
  dom.conversationList.innerHTML = "";
  chatConversations.forEach((conversation) => {
    const card = document.createElement("button");
    card.type = "button";
    card.className = `conversation-card ${conversation.id === activeConversationId ? "active" : ""}`;
    card.innerHTML = `<strong>${conversation.seller}</strong><p>${conversation.itemTitle}</p><span>${conversation.preview}</span>`;
    card.addEventListener("click", () => {
      activeConversationId = conversation.id;
      renderChatSidebar();
      renderChatThread();
    });
    dom.conversationList.appendChild(card);
  });
}

function renderChatThread() {
  const conversation = chatConversations.find((entry) => entry.id === activeConversationId);
  if (!conversation) return;
  dom.threadTitle.textContent = `${conversation.seller} · ${conversation.itemTitle}`;
  dom.messageThread.innerHTML = "";
  const closeMessageMenus = () => {
    dom.messageThread.querySelectorAll(".message-context-menu").forEach((menu) => menu.remove());
  };
  conversation.messages.forEach((message) => {
    const bubble = document.createElement("article");
    bubble.className = `message-bubble ${message.self ? "self" : ""}`;
    const text = document.createElement("span");
    text.textContent = message.recalled ? t("recalledMessage") : message.text;
    bubble.appendChild(text);
    if (message.self && !message.recalled) {
      bubble.addEventListener("contextmenu", (event) => {
        event.preventDefault();
        closeMessageMenus();
        const menu = document.createElement("div");
        menu.className = "message-context-menu";
        const copyButton = document.createElement("button");
        copyButton.type = "button";
        copyButton.className = "text-button";
        copyButton.textContent = t("copy");
        copyButton.addEventListener("click", async () => {
          try {
            await copyMessageText(message.text);
            copyButton.textContent = t("copied");
            setTimeout(() => {
              closeMessageMenus();
            }, 500);
          } catch {
            closeMessageMenus();
          }
        });
        menu.appendChild(copyButton);

        const recallButton = document.createElement("button");
        recallButton.type = "button";
        recallButton.className = "text-button";
        const recallable = canRecallMessage(message);
        recallButton.textContent = recallable ? t("recall") : t("recallExpired");
        recallButton.disabled = !recallable;
        if (recallable) {
          recallButton.addEventListener("click", () => {
            message.recalled = true;
            renderChatThread();
          });
        }
        menu.appendChild(recallButton);
        bubble.appendChild(menu);
      });
    }
    bubble.addEventListener("click", closeMessageMenus);
    dom.messageThread.appendChild(bubble);
  });
  dom.messageThread.addEventListener(
    "click",
    () => {
      closeMessageMenus();
    },
    { once: true }
  );
}

function openChatView() {
  buildChatConversations();
  applyChatCopy();
  renderChatSidebar();
  renderChatThread();
  pendingOrderItemId = null;
  showView("chat");
}

function setLanguage(language) {
  currentLanguage = language;
  localStorage.setItem(LANGUAGE_KEY, language);
  applyStaticText();
  populateCategories();
  renderListings();
  renderWantedPosts();
  renderOrdersView();
  renderCart();
  if (activeView === "detail") {
    renderDetailView();
  }
  if (activeView === "chat") {
    buildChatConversations();
    renderChatSidebar();
    renderChatThread();
  }
}

function attachEvents() {
  [dom.searchInput, dom.categoryFilter, dom.conditionFilter, dom.sortFilter].forEach((element) => {
    element.addEventListener("input", renderListings);
    element.addEventListener("change", renderListings);
  });

  dom.priceRange.addEventListener("input", () => {
    dom.priceValue.textContent = dom.priceRange.value;
    renderListings();
  });
  dom.showFavoritesButton.addEventListener("click", () => {
    state.showFavoritesOnly = !state.showFavoritesOnly;
    dom.showFavoritesButton.textContent = state.showFavoritesOnly ? t("showingFavorites") : t("favorites");
    renderListings();
  });
  dom.resetFiltersButton.addEventListener("click", resetFilters);
  dom.checkoutButton.addEventListener("click", openCheckoutView);
  document.getElementById("generateAiCopy").addEventListener("click", createAiDescription);
  dom.imageInput.addEventListener("change", handleListingImageChange);
  dom.listingForm.addEventListener("submit", handleFormSubmit);
  dom.wantedForm.addEventListener("submit", handleWantedSubmit);
  dom.jumpToSell.addEventListener("click", () => {
    setPrimarySection("sell");
  });
  dom.modeBrowse.addEventListener("click", () => {
    setPrimarySection("browse");
  });
  dom.modeSell.addEventListener("click", () => {
    setPrimarySection("sell");
  });
  dom.modeWanted.addEventListener("click", () => {
    setPrimarySection("wanted");
  });
  dom.studentVerifiedButton.addEventListener("click", () => showView("auth"));
  dom.exploreNow.addEventListener("click", () => {
    setPrimarySection("browse");
  });
  dom.loginLink.addEventListener("click", () => showView("auth"));
  dom.joinNowLink.addEventListener("click", () => showView("auth"));
  dom.myHubToggle.addEventListener("click", (event) => {
    event.stopPropagation();
    toggleMyHub();
  });
  dom.myHubPanel.addEventListener("click", (event) => {
    event.stopPropagation();
  });
  dom.myHubMessages.addEventListener("click", () => {
    closeMyHub();
    openChatView();
  });
  dom.myHubCart.addEventListener("click", () => {
    closeMyHub();
    setPrimarySection("browse");
    dom.cartPanel.scrollIntoView({ behavior: "smooth", block: "start" });
  });
  dom.myHubOrders.addEventListener("click", () => {
    closeMyHub();
    renderOrdersView();
    showView("orders");
  });
  dom.menuToggle.addEventListener("click", (event) => {
    event.stopPropagation();
    toggleNavbarMenu();
  });
  document.querySelectorAll('[data-view-target="auth"]').forEach((button) => button.addEventListener("click", () => showView("auth")));
  document.querySelectorAll('[data-view-target="chat"]').forEach((button) => button.addEventListener("click", openChatView));
  document.querySelectorAll("[data-detail-id]").forEach((button) =>
    button.addEventListener("click", () => openDetailView(Number(button.dataset.detailId)))
  );
  document.querySelectorAll("[data-scroll-target]").forEach((button) =>
    button.addEventListener("click", () => {
      document.getElementById(button.dataset.scrollTarget).scrollIntoView({ behavior: "smooth" });
    })
  );
  dom.langEn.addEventListener("click", () => setLanguage("en"));
  dom.langZh.addEventListener("click", () => setLanguage("zh"));
  document.querySelectorAll(".view-back-button").forEach((button) => {
    button.addEventListener("click", hideViews);
  });
  dom.loginTab.addEventListener("click", () => setAuthTab(true));
  dom.registerTab.addEventListener("click", () => setAuthTab(false));
  [dom.loginForm, dom.registerForm].forEach((form) => {
    form.addEventListener("submit", (event) => {
      event.preventDefault();
      hideViews();
    });
  });
  dom.detailCartButton.addEventListener("click", () => addToCart(activeDetailId));
  dom.chatSellerLink.addEventListener("click", openChatView);
  document.getElementById("makeOfferLink").addEventListener("click", () => showView("auth"));
  document.addEventListener("click", () => {
    closeMyHub();
  });
  dom.checkoutForm.addEventListener("submit", (event) => {
    event.preventDefault();
    const orderedItems = [...state.cart];
    const orderId = `CX${Date.now().toString().slice(-8)}`;
    const total = formatCurrency(orderedItems.reduce((sum, item) => sum + item.price * item.quantity, 0));
    const itemsSummary = orderedItems.map((item) => `${getListingText(item, "title")} x${item.quantity}`).join(", ");
    const pickupValue = document.getElementById("checkoutPickup").value.trim();
    const timeValue = document.getElementById("checkoutTime").value.trim();
    const contactValue = document.getElementById("checkoutPhone").value.trim();
    pendingOrderItemId = orderedItems[0]?.id || null;
    pendingOrderMessage =
      currentLanguage === "zh"
        ? `我刚提交了订单 ${orderId}，希望在${pickupValue}于${timeValue}交接，可以的话请回复我。`
        : `I just placed order ${orderId}. Could we meet at ${pickupValue} around ${timeValue}? Please let me know if that works.`;
    state.orders.unshift({
      id: orderId,
      itemsSummary,
      pickup: pickupValue,
      time: timeValue,
      contact: contactValue,
      total,
    });
    document.getElementById("checkoutPageStatus").textContent = t("checkoutSuccess");
    document.getElementById("checkoutOrderIdValue").textContent = orderId;
    document.getElementById("checkoutPickupConfirmValue").textContent = pickupValue;
    document.getElementById("checkoutTimeConfirmValue").textContent = timeValue;
    document.getElementById("checkoutContactConfirmValue").textContent = contactValue;
    dom.checkoutForm.classList.add("hidden-view");
    dom.checkoutConfirmation.classList.remove("hidden-view");
    state.cart = [];
    persistState();
    renderCart();
    renderCheckoutView();
    renderOrdersView();
    setTimeout(() => {
      openChatView();
    }, 1100);
  });
  dom.chatComposer.addEventListener("submit", (event) => {
    event.preventDefault();
    const text = dom.composerInput.value.trim();
    if (!text) return;
    const conversation = chatConversations.find((entry) => entry.id === activeConversationId);
    conversation.messages.push({ id: Date.now(), self: true, text, recalled: false, sentAt: Date.now() });
    dom.composerInput.value = "";
    renderChatThread();
  });
}

attachEvents();
populateCategories();
applyStaticText();
dom.menuToggle.setAttribute("aria-expanded", dom.navbarActions.classList.contains("open") ? "true" : "false");
dom.menuToggle.textContent = dom.navbarActions.classList.contains("open") ? t("closeMenu") : t("menu");
setPrimarySection("browse", { smooth: false });
renderListings();
renderWantedPosts();
renderCart();
renderCheckoutView();
renderOrdersView();
renderDetailView();
buildChatConversations();
renderChatSidebar();
renderChatThread();
hideViews();
