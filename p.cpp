template <typename T>
class Pool {
    private:
    std::vector<T> data;

    public:
    Pool(int size = 100) {Resize(size); }
    ~Pool()) = default;

    bool IsEmpty() const { return data.empt(); }
    int GetSize() const { return data.size();}
    void Resize(int n) {data.resize(n); }
    void Clear() {data.clear(); }
    void Add(T object) {data.push_back(object)}
    void Set(int Index, T object) {data[index] = object; }
    T& Get(int index) {return static_cast<T&>{data[index]};}

    T& operator [](unasigned int indeex){ return data [index]}

};