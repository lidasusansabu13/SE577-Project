export interface RepositoryApiInterface {
    id: number;
    name: string;
    description: string;
    open_issues: number;
    forks: number;
    language: string;

}

export interface UserApiInterface{
    login: string;
    avatar_url : string;
    email : string;
    name: string;
    bio : string;
    public_repos : number;
    followers : number;
    following : number;
}

export interface PrApiInterface{
    title: string;
    number : number;
    created_at : string;
}